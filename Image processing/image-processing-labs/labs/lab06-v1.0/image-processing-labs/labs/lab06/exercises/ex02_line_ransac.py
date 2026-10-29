"""Core: compare an all-point line fit with a two-point RANSAC fit."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 0
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]


def ordinary_line(points: np.ndarray) -> np.ndarray:
    vx, vy, x0, y0 = cv2.fitLine(points.reshape(-1, 1, 2), cv2.DIST_L2, 0, 0.01, 0.01).reshape(-1)
    return np.array([-vy, vx, vy * x0 - vx * y0], np.float64)


def distances_to_line(points: np.ndarray, line: np.ndarray) -> np.ndarray:
    a, b, c = line
    return np.abs(a * points[:, 0] + b * points[:, 1] + c) / np.sqrt(a * a + b * b)


def process(frame: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width) // 3
    top, left = (height - side) // 2, (width - side) // 2
    crop = frame[top:top + side, left:left + side]
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, ink = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Ransac works on points, not masks
    rows, columns = np.nonzero(ink)
    points = np.column_stack([columns, rows]).astype(np.float32)

    if len(points) < 2:
        return [("Full camera frame: crop in green", full_view),
                ("Selected evidence", crop), ("Segmented ink", ink),
                ("Not enough points for line fitting", crop.copy())]

    # RANSAC: sample two pixels, build a line, and count inliers.
    # Do this until many trials have been performed and then only keep the best line, then do OLS with inliers only.
    max_iter = 300
    threshold = 0.02 * side  # px
    generator = np.random.default_rng(42)
    best_inliers_mask = np.zeros(len(points), dtype=bool)
    for _ in range(max_iter):
        # TODO: write one RANSAC iteration.
        # 1. Draw two different indices
        #    and build the candidate line through those two points with ordinary_line.
        # 2. Measure every point's distance to the candidate with distances_to_line.
        # 3. inliers_mask = points whose distance is at most threshold (a boolean array).
        # 4. If inliers_mask has more inliers than best_inliers_mask, keep it as the best.
        line = ordinary_line(points[generator.choice(len(points),2,replace=False)])
        distances = distances_to_line(points,line)
        inlier_masks = distances <= threshold
        if inlier_masks.sum() > best_inliers_mask.sum():
            best_inliers_mask = inlier_masks


    baseline = ordinary_line(points)
    robust = ordinary_line(points[best_inliers_mask])

    # Draw each line across the crop, solving ax + by + c = 0 for y or x.
    comparison = crop.copy()
    for line, colour in ((baseline, (0, 0, 220)), (robust, (0, 180, 0))):
        a, b, c = line
        if abs(b) >= abs(a):  # Mostly horizontal: use left and right edges.
            first = (0, round(-c / b))
            second = (side - 1, round(-(a * (side - 1) + c) / b))
        else:  # Mostly vertical: use top and bottom edges.
            first = (round(-c / a), 0)
            second = (round(-(b * (side - 1) + c) / a), side - 1)
        cv2.line(comparison, first, second, colour, 2, cv2.LINE_AA)

    # Red foreground votes, with the best candidate's inliers coloured green.
    evidence_box = cv2.cvtColor(ink, cv2.COLOR_GRAY2BGR)
    evidence_box[rows, columns] = (0, 0, 220)
    evidence_box[rows[best_inliers_mask], columns[best_inliers_mask]] = (0, 165, 0)

    return [("Full camera frame: crop in green", full_view),
            ("Selected evidence", crop), 
            ("Segmented ink", ink),
            ("Red ordinary / green robust", comparison),
            (f"All votes: {best_inliers_mask.sum()}/{len(points)} green inliers", evidence_box)
            ]


def main() -> None:
    print("Center the stroke to analyze in the small green square. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 6 - line RANSAC",
                           make_montage(process(frame), columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
