"""Optional: detect 24 patches, then capture their color matrix for live use."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 1
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0),
            # manually distort color settings to simulate an issue to correct
            ("auto white balance", cv2.CAP_PROP_AUTO_WB, 0.0),
            ("white balance temperature", cv2.CAP_PROP_WB_TEMPERATURE, 6500.0),
            ("hue", cv2.CAP_PROP_HUE, 40.0)]

# Source artwork in gamma-encoded RGB, row-major on the printed 4 x 6 chart.
REFERENCE_RGB = np.array([
    [0.72, 0.22, 0.20], [0.24, 0.55, 0.25], [0.18, 0.32, 0.72],
    [0.72, 0.60, 0.14], [0.58, 0.22, 0.62], [0.16, 0.62, 0.64],
    [0.82, 0.38, 0.14], [0.38, 0.24, 0.68], [0.20, 0.68, 0.34],
    [0.74, 0.18, 0.38], [0.18, 0.48, 0.70], [0.68, 0.48, 0.20],
    [0.62, 0.34, 0.22], [0.26, 0.42, 0.62], [0.48, 0.62, 0.22],
    [0.70, 0.32, 0.52], [0.20, 0.58, 0.50], [0.56, 0.44, 0.70],
    [0.78, 0.78, 0.78], [0.64, 0.64, 0.64], [0.50, 0.50, 0.50],
    [0.36, 0.36, 0.36], [0.23, 0.23, 0.23], [0.11, 0.11, 0.11],
], np.float64)


def process(frame: np.ndarray, captured_matrix: np.ndarray | None = None):
    """Return labelled panels and a matrix available for capture, or None."""
    height, width = frame.shape[:2]
    side = min(height, width)
    top, left = (height - side) // 2, (width - side) // 2
    crop = frame[top:top + side, left:left + side]
    rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float64) / 255.0
    matrix = captured_matrix
    candidate_matrix = None

    if captured_matrix is None:
        # threshold and label patches together with the other printed graphics
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        paper = float(np.percentile(gray, 95))
        mask = cv2.inRange(gray, 0, round(0.85 * paper))
        count, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=4)

        # keep filled squares in the chart region, using relative measurements
        accepted = []
        for label in range(1, count):  # label 0 is the background
            _, _, box_width, box_height, area = stats[label]
            center_x, center_y = centroids[label]
            # TODO: compute the relative area, aspect ratio, and fill ratio of this
            # component and append label to accepted only when they and its centroid
            # are plausible for a colour patch
            raise NotImplementedError("Filter the patch components")

        if len(accepted) != 24:
            full_view = frame.copy()
            cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)
            return [("Full camera frame: crop in green", full_view),
                    ("Camera card", crop),
                    (f"Expected 24 patches, found {len(accepted)}", mask)], None

        # sort into four rows, then left to right within each row
        accepted = sorted(accepted, key=lambda label: centroids[label, 1])
        ordered = []
        for row in range(4):
            ordered.extend(sorted(accepted[row * 6:(row + 1) * 6], key=lambda label: centroids[label, 0]))

        # sample patch interiors; store positions and rectangles for drawing later
        measured = []
        positions = []
        for label in ordered:
            x, y = np.rint(centroids[label]).astype(int)
            half_width = max(2, stats[label, cv2.CC_STAT_WIDTH] // 4)
            half_height = max(2, stats[label, cv2.CC_STAT_HEIGHT] // 4)
            positions.append((x, y, half_width, half_height))
            patch = rgb[y - half_height:y + half_height + 1, x - half_width:x + half_width + 1]
            measured.append(patch.mean(axis=(0, 1)))
        measured = np.asarray(measured)

        # fit measured @ matrix to the reference RGB pairs, as in Ex03 (np.linalg.lstsq is numerically more stable)
        reference = np.rint(REFERENCE_RGB * 255) / 255
        matrix, _, _, _ = np.linalg.lstsq(measured, reference, rcond=None)
        # matrix = np.linalg.inv(measured.T @ measured) @ measured.T @ reference
        candidate_matrix = matrix

    # apply the matrix to every pixel; a captured matrix is never refitted
    corrected_rgb = np.clip(rgb.astype(np.float32) @ matrix, 0.0, 1.0)
    corrected = cv2.cvtColor(np.rint(corrected_rgb * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

    # visualization and debugging
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)
    if captured_matrix is not None:
        return [("Full camera frame: crop in green", full_view),
                ("Live camera crop", crop),
                ("Captured matrix; restart to reset", corrected)], None

    annotated = crop.copy()
    for index, (x, y, half_width, half_height) in enumerate(positions, 1):
        cv2.rectangle(annotated, (x - half_width, y - half_height),
                      (x + half_width, y + half_height), (255, 255, 255), 2)
        cv2.putText(annotated, str(index), (x - 12, y + 7),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
        
    return [("Full camera frame: crop in green", full_view),
            ("Threshold: patches + printed graphics", mask),
            ("24 patches found; press C to capture", annotated),
            ("Live 24-patch normalization", corrected)], candidate_matrix


def main() -> None:
    captured_matrix = None
    print("Fill the green square with the colour chart under fixed light.")
    print("When all 24 patches are labelled, press C to capture the matrix.")
    print("Q quits and restores the camera controls.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                panels, candidate_matrix = process(frame, captured_matrix)
                cv2.imshow("Lecture 5 - complete chart", make_montage(panels, columns=2, panel_width=360))
                key = cv2.waitKey(1) & 0xFF
                if key in (ord("c"), ord("C")) and captured_matrix is None:
                    if candidate_matrix is None:
                        print("Chart rejected: show all 24 patches under even light before capturing.")
                    else:
                        captured_matrix = candidate_matrix.copy()
                        print("Captured matrix; restart the script to reset it:\n", captured_matrix)
                if key in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
