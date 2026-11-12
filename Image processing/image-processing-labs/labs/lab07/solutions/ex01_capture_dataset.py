"""Core: capture varied live views with refined checkerboard corner feedback."""

from functools import cache
from pathlib import Path

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

LAB = Path(__file__).resolve().parents[1]
CAMERA_ID = 1
REQUESTS = [
    ("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
    ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0),
    ("autofocus", cv2.CAP_PROP_AUTOFOCUS, 0.0),  # refocusing moves the lens and changes the intrinsics
    ("focus", cv2.CAP_PROP_FOCUS, 350.0),
]

# The course webcam has almost no lens distortion, so every frame gets a known
# barrel distortion in software, like a cheap wide-angle lens, for calibration
# to recover. Set both coefficients to 0.0 to see the real camera.
ADDED_FOCAL_PX = 600.0
ADDED_K1_K2 = (-0.25, 0.05)  # radial terms of OpenCV's lens model; negative k1 is barrel

DATASET = LAB / "outputs" / "calibration"
PATTERN = (9, 6)  # internal corners: they are well-defined points, unlike the card's outer edge


@cache  # one map per resolution; each frame then costs only a remap
def _lens_maps(width: int, height: int) -> tuple[np.ndarray, np.ndarray]:
    k1, k2 = ADDED_K1_K2
    cx, cy = (width - 1) / 2, (height - 1) / 2
    yy, xx = np.indices((height, width), dtype=np.float32)
    r_distorted = np.hypot(xx - cx, yy - cy) / ADDED_FOCAL_PX
    # remap asks where each output pixel comes from, so the lens model is
    # inverted: tabulate ideal -> distorted radius and read it backwards.
    r_ideal = np.linspace(0.0, 3.0, 6001)
    r_lens = r_ideal * (1 + k1 * r_ideal**2 + k2 * r_ideal**4)
    if np.any(np.diff(r_lens) <= 0) or r_lens[-1] < r_distorted.max():
        raise ValueError("ADDED_K1_K2 folds the image; use a weaker distortion")
    scale = np.interp(r_distorted, r_lens, r_ideal) / np.maximum(r_distorted, 1e-9)
    scale[r_distorted < 1e-9] = 1.0
    return (cx + (xx - cx) * scale).astype(np.float32), (cy + (yy - cy) * scale).astype(np.float32)


def add_lens_distortion(frame: np.ndarray) -> np.ndarray:
    map_x, map_y = _lens_maps(frame.shape[1], frame.shape[0])
    return cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)  # black where the "lens" sees outside the sensor


def detect_corners(frame: np.ndarray) -> np.ndarray | None:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(
        gray,
        PATTERN,
        cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE,  # tolerate uneven light on the print
    )
    if not found:  # a partial grid cannot be matched to the board's known geometry
        return None
    # Detection is only pixel-accurate; calibration needs sub-pixel corners.
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
    refined = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return refined.reshape(-1, 1, 2)


def process(frame: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width)
    x, y = (width - side) // 2, (height - side) // 2
    crop = frame[y:y + side, x:x + side]  # no resize: feedback uses the camera's own pixels
    full = frame.copy()
    cv2.rectangle(full, (x, y), (x + side - 1, y + side - 1), (0, 255, 0), 2)
    corners = detect_corners(crop)
    annotated = crop.copy()
    # The coloured ordering shows whether corner 1 stays at the same physical corner.
    cv2.drawChessboardCorners(annotated, PATTERN, corners, corners is not None)
    status = "54 refined corners" if corners is not None else "Missing corners: reframe, tilt less, check focus"
    return [("Full frame: crop in green", full), ("Actual card crop", crop), (status, annotated)]


def save_view(frame: np.ndarray, directory: Path = DATASET):
    # Save the full frame so intrinsic coordinates do not use the display crop.
    directory.mkdir(parents=True, exist_ok=True)
    # Continue after the highest existing view so resuming never overwrites.
    number = max((int(p.stem.split("_")[-1]) for p in directory.glob("view_*.png")), default=0) + 1
    path = directory / f"view_{number:02d}.png"
    if not cv2.imwrite(str(path), frame):
        raise RuntimeError(f"Could not save {path}")
    return path


def main() -> None:
    print("H saves the current frame; Q quits. Vary the card's position, distance, and tilt.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for raw in frames:
                frame = add_lens_distortion(raw)  # everything downstream sees only the distorted camera
                panels = process(frame)
                cv2.imshow("Lecture 7 - capture dataset", make_montage(panels, columns=3, panel_width=360))
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                if key == ord("h"):  # save the distorted full frame, not the annotated crop
                    print(save_view(frame, DATASET))
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
