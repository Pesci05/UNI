"""Core: fit captured views once, then undistort new live frames at fixed focus."""

from pathlib import Path

import cv2
import numpy as np

from labs.common import camera_frames, make_montage
# Same detector as capture: the corners you checked live are the ones that get fitted.
# Same added lens: the live camera must be the one that was calibrated.
from labs.lab07.solutions.ex01_capture_dataset import (
    PATTERN,
    add_lens_distortion,
    detect_corners,
)

# Where the views come from and where the reprojection evidence goes.
LAB = Path(__file__).resolve().parents[1]
HELD_OUT = LAB / "assets" / "calibration_held_out.png"
CALIBRATION = LAB / "assets" / "calibration"
DATASET = LAB / "outputs" / "calibration"
REPROJECTION = LAB / "outputs" / "reprojection"  # kept apart: view_*.png in DATASET are fitting inputs
RESIDUAL_SCALE = 50  # residuals are sub-pixel, so their drawn length is exaggerated
SQUARE_SIZE_MM = 10.0  # printed square side: sets the units of the board poses (t in mm)
# Live camera: identical requests to ex01, or the fitted K does not apply.
CAMERA_ID = 1
FOCUS = 350.0  # Driver units: must match the value used for dataset capture.
REQUESTS = [
    ("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
    ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0),
    ("autofocus", cv2.CAP_PROP_AUTOFOCUS, 0.0),
    ("focus", cv2.CAP_PROP_FOCUS, FOCUS),
]


def calibrate(directory: Path = DATASET, square_size_mm: float = SQUARE_SIZE_MM):
    """Fit K and distortion; return them with per-view errors, overall RMS, and per-view
    (path, detected corners, reprojected corners, rvec, tvec)."""
    # 1. Board corners in world coordinates (3-D points, the same for every view).
    # The board defines the world frame: flat (Z = 0), corners on a known grid.
    # Square size only sets the units of the poses; K stays in pixels.
    template = np.zeros((PATTERN[0] * PATTERN[1], 3), np.float32)
    template[:, :2] = np.mgrid[0 : PATTERN[0], 0 : PATTERN[1]].T.reshape(-1, 2)
    if square_size_mm <= 0:
        raise ValueError("Square size must be positive")
    template *= square_size_mm
    # 2. Detected corners in each saved view (2-D pixels), paired with the template.
    object_points, image_points = [], []
    image_size = None
    used_paths = []
    for path in sorted(directory.glob("view_*.png")):
        frame = cv2.imread(path)
        size = (frame.shape[1], frame.shape[0])
        if image_size is not None and size != image_size:  # K is measured in pixels of one resolution
            raise ValueError("Calibration views must all have the same resolution")
        image_size = size
        corners = detect_corners(frame)
        if corners is not None:  # incomplete views are skipped: their corners cannot be matched
            object_points.append(template.copy())  # the same physical board seen in every view
            image_points.append(corners)
            used_paths.append(path)
        else:
            print(f"{path.name}: skipped, corners not found")
    if not image_points or image_size is None:
        raise RuntimeError(f"No usable calibration views in {directory}")
    if len(image_points) < 6:  # allowed, to see the effect; K and distortion are poorly constrained
        print(f"Warning: only {len(image_points)} usable views; the fit may not transfer to new frames")
    # 3. The fit: intrinsics (K, distortion) shared by all views, one pose (rvec, tvec) per view.
    rms, camera_matrix, distortion, rvecs, tvecs = cv2.calibrateCamera(
        object_points,
        image_points,
        image_size,
        None,
        None,
        flags=cv2.CALIB_FIX_K3,  # k3 mostly fits noise at the image corners of a webcam lens
    )
    # 4. Quality check: re-project the board with the fitted model and compare with detections.
    # The RMS averages over all views; per-view errors point at the bad ones.
    errors, views = [], []
    fitted = zip(used_paths, object_points, image_points, rvecs, tvecs, strict=True)
    for path, world, observed, rvec, tvec in fitted:
        projected, _ = cv2.projectPoints(world, rvec, tvec, camera_matrix, distortion)
        differences = observed.reshape(-1, 2) - projected.reshape(-1, 2)
        errors.append(float(np.sqrt(np.mean(np.sum(differences * differences, axis=1)))))
        # The extrinsics come for free: each view's board pose in camera coordinates.
        views.append((path, observed.reshape(-1, 2), projected.reshape(-1, 2), rvec, tvec))
    return camera_matrix, distortion, np.asarray(errors), float(rms), views


def draw_reprojection(frame: np.ndarray, view, error: float, camera_matrix, distortion, axis_length: float):
    # Green circles: detected corners. Red crosses: the board re-projected by the fitted model.
    # Yellow lines: residual from detected to projected, drawn RESIDUAL_SCALE times longer.
    _, observed, projected, rvec, tvec = view
    image = frame.copy()
    for (ox, oy), (px, py) in zip(observed, projected, strict=True):
        tip = (ox + RESIDUAL_SCALE * (px - ox), oy + RESIDUAL_SCALE * (py - oy))
        cv2.line(image, (round(ox), round(oy)), (round(tip[0]), round(tip[1])), (0, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(image, (round(ox), round(oy)), 4, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.drawMarker(image, (round(px), round(py)), (0, 0, 255), cv2.MARKER_CROSS, 8, 1, cv2.LINE_AA)
    # Board frame at corner 1, from this view's R, t: X red, Y green, Z = X x Y blue.
    cv2.drawFrameAxes(image, camera_matrix, distortion, rvec, tvec, axis_length, 2)
    text = f"RMS {error:.3f} px, residuals x{RESIDUAL_SCALE}, board {np.linalg.norm(tvec):.0f} mm away"
    cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    return image


def process(frame: np.ndarray, calibration, image_size: tuple[int, int], reference: np.ndarray | None = None):
    if (frame.shape[1], frame.shape[0]) != image_size:  # a mismatched K would be silently wrong
        raise ValueError("Frame resolution differs from the fitted calibration; recapture at this resolution")
    camera_matrix, distortion = calibration[:2]
    # Only the lens model is inverted; perspective is geometry, not a lens defect.
    undistorted = cv2.undistort(frame, camera_matrix, distortion)
    panels = [("New frame: lens distortion and perspective", frame),
              ("Undistorted: perspective remains", undistorted)]
    if reference is not None:  # the undistorted panel should match this one, not a flat card
        panels.insert(0, ("Camera frame before the added lens", reference))
    return panels


def main() -> None:
    paths = sorted(DATASET.glob("view_*.png"))
    if not paths:
        raise RuntimeError("Run ex01_capture_dataset.py first to capture a fixed-focus dataset.")
    first = cv2.imread(paths[0])
    image_size = (first.shape[1], first.shape[0])
    calibration = calibrate(DATASET, SQUARE_SIZE_MM)  # fitted once, before the camera opens
    camera_matrix, distortion, errors, rms, views = calibration

    # Evaluate the fit: per-view errors, reprojection images, and the recovered extrinsics.
    REPROJECTION.mkdir(parents=True, exist_ok=True)
    for old in REPROJECTION.glob("view_*.png"):  # the folder always shows the latest fit only
        old.unlink()
    print(f"Per-view reprojection errors (images and extrinsics.txt in {REPROJECTION}):")
    poses = []
    for view, error in zip(views, errors, strict=True):
        path, _, _, rvec, tvec = view
        flag = "  <- several times the median: check this view" if error > 3 * np.median(errors) else ""
        print(f"  {path.name}: {error:.3f} px{flag}")
        axis_length = 3 * SQUARE_SIZE_MM  # three squares, in the board's units
        drawing = draw_reprojection(cv2.imread(path), view, error, camera_matrix, distortion, axis_length)
        if not cv2.imwrite(str(REPROJECTION / path.name), drawing):
            raise RuntimeError(f"Could not save {REPROJECTION / path.name}")
        rotation, _ = cv2.Rodrigues(rvec)  # rotation vector -> 3x3 matrix R
        # X_camera = R @ X_board + t: board millimetres to camera millimetres.
        rows = np.array2string(rotation, precision=4)
        poses.append(f"{path.name}\nR =\n{rows}\nt (mm) = {np.array2string(tvec.ravel(), precision=1)}\n")
    (REPROJECTION / "extrinsics.txt").write_text("\n".join(poses), encoding="utf-8")
    print(f"Overall RMS={rms:.4f}px over {len(views)} views")
    print("K=\n", camera_matrix, "\ndistortion=", distortion.ravel())

    # Apply the fixed model to live frames that were never part of the fit.
    print("Q quits. The model is fitted once; keep camera zoom unchanged.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for raw in frames:
                panels = process(add_lens_distortion(raw), calibration, image_size, reference=raw)
                cv2.imshow("Lecture 7 - live undistortion", make_montage(panels, columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
