"""Optional: extend RANSAC by changing sample, model, and residual."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 1
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]


def ordinary_ellipse(points: np.ndarray):
    return cv2.fitEllipse(points.reshape(-1, 1, 2))


def distances_to_ellipse(points: np.ndarray, ellipse, image_shape: np.ndarray) -> np.ndarray:
    """Pixel distances to the candidate ellipse boundary visible in the crop."""
    columns, rows = points.astype(int).T
    boundary = np.full(image_shape, 255, np.uint8)
    cv2.ellipse(boundary, ellipse, 0, 1, cv2.LINE_8)
    distances = cv2.distanceTransform(boundary, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
    return distances[rows, columns]


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

    if len(points) < 5:
        return [("Full camera frame: crop in green", full_view),
                ("Selected evidence", crop), ("Segmented ink", ink),
                ("Not enough points for ellipse fitting", crop.copy())]

    # RANSAC: sample five pixels, build an ellipse, and count inliers.
    max_iter = 300
    threshold = 0.025 * side  # distance to the candidate boundary in pixels
    generator = np.random.default_rng(42)
    best_inliers_mask = np.zeros(len(points), dtype=bool)
    for _ in range(max_iter):
        ellipse = ordinary_ellipse(points[generator.choice(len(points), 5, replace=False)])
        distances = distances_to_ellipse(points, ellipse, ink.shape)
        inliers_mask = distances <= threshold
        if inliers_mask.sum() > best_inliers_mask.sum():
            best_inliers_mask = inliers_mask

    baseline = ordinary_ellipse(points)
    robust = ordinary_ellipse(points[best_inliers_mask])

    # Draw both fitted ellipses on the same crop.
    comparison = crop.copy()
    for ellipse, colour in ((baseline, (0, 0, 220)), (robust, (0, 180, 0))):
        cv2.ellipse(comparison, ellipse, colour, 2, cv2.LINE_AA)

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
    print("Center the curved stroke to analyze in the small green square. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 6 - ellipse RANSAC",
                           make_montage(process(frame), columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
