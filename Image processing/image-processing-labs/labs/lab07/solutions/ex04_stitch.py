"""Optional: compare direct and robust stitching from visible matches."""

from pathlib import Path

import cv2
import numpy as np

from labs.common import make_montage

LAB = Path(__file__).resolve().parents[1]
ASSETS = LAB / "assets"

# Rows correspond one-to-one. The last right-hand point is deliberately false.
LEFT_POINTS = np.float32(
    [
        [450, 100],
        [600, 120],
        [760, 90],
        [470, 260],
        [620, 250],
        [740, 350],
        [500, 410],
        [690, 400],
    ]
)
RIGHT_POINTS = np.float32(
    [
        [62.184937, 105.28462],
        [205.50146, 122.19362],
        [359.6122, 91.3629],
        [76.40576, 259.2378],
        [222.52628, 247.49535],
        [338.87314, 344.7798],
        [101.24198, 407.8594],
        [364.10043, 335.53046],  # false: displaced by (+75, -60)
    ]
)


def estimate_homographies() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Right maps onto left, so the left view stays the reference frame.
    direct, _ = cv2.findHomography(RIGHT_POINTS, LEFT_POINTS, method=0)  # least squares: every match pulls
    # Matches that reproject within 3 px of the consensus model count as inliers.
    robust, inliers = cv2.findHomography(RIGHT_POINTS, LEFT_POINTS, cv2.RANSAC, 3.0)
    if direct is None or robust is None or inliers is None:
        raise RuntimeError("Could not estimate both homographies")
    return direct, robust, inliers.ravel().astype(bool)


def warp_pair(left: np.ndarray, right: np.ndarray, homography: np.ndarray) -> np.ndarray:
    right_corners = np.float32(
        [[0, 0], [right.shape[1], 0], [right.shape[1], right.shape[0]], [0, right.shape[0]]]
    )
    warped = cv2.perspectiveTransform(right_corners.reshape(-1, 1, 2), homography).reshape(-1, 2)
    left_corners = np.float32(
        [[0, 0], [left.shape[1], 0], [left.shape[1], left.shape[0]], [0, left.shape[0]]]
    )
    # The warped view can land at negative coordinates; shift both views so the canvas holds them.
    all_corners = np.vstack([warped, left_corners])
    minimum = np.floor(all_corners.min(axis=0)).astype(int)
    maximum = np.ceil(all_corners.max(axis=0)).astype(int)
    translation = np.array([[1, 0, -minimum[0]], [0, 1, -minimum[1]], [0, 0, 1]], np.float64)
    size = tuple((maximum - minimum).astype(int))

    result = cv2.warpPerspective(right, translation @ homography, size, borderValue=(238,) * 3)
    right_mask = cv2.warpPerspective(
        np.full(right.shape[:2], 255, np.uint8), translation @ homography, size
    )
    x, y = -minimum
    region = result[y : y + left.shape[0], x : x + left.shape[1]]
    overlap = right_mask[y : y + left.shape[0], x : x + left.shape[1]] > 0
    region[~overlap] = left[~overlap]
    # Averaging, not overwriting, turns any misalignment into visible ghosting.
    region[overlap] = (
        (region[overlap].astype(np.uint16) + left[overlap].astype(np.uint16)) // 2
    ).astype(np.uint8)
    return result


def draw_matches(left: np.ndarray, right: np.ndarray, inliers: np.ndarray) -> np.ndarray:
    canvas = np.hstack([left, right])
    offset = np.array([left.shape[1], 0])
    correspondences = zip(LEFT_POINTS, RIGHT_POINTS, inliers, strict=True)
    for index, (left_point, right_point, accepted) in enumerate(correspondences, 1):
        first = tuple(np.rint(left_point).astype(int))
        second = tuple(np.rint(right_point + offset).astype(int))
        colour = (0, 170, 0) if accepted else (0, 0, 230)
        cv2.line(canvas, first, second, colour, 2, cv2.LINE_AA)
        cv2.circle(canvas, first, 6, colour, -1)
        cv2.circle(canvas, second, 6, colour, -1)
        cv2.putText(canvas, str(index), first, cv2.FONT_HERSHEY_SIMPLEX, 0.6, colour, 2)
    return canvas


def stitch(left: np.ndarray, right: np.ndarray):
    direct, robust, inliers = estimate_homographies()
    return warp_pair(left, right, direct), warp_pair(left, right, robust), inliers


def process(_: np.ndarray | None = None):
    left = cv2.imread(ASSETS / "stitch_left.png")
    right = cv2.imread(ASSETS / "stitch_right.png")
    direct, robust, inliers = stitch(left, right)
    print(f"RANSAC inliers: {inliers.tolist()}")
    return [
        ("Seven green matches and one false red match", draw_matches(left, right, inliers)),
        ("Direct homography: all eight matches", direct),
        ("RANSAC homography: seven inliers", robust),
    ]


def main() -> None:
    montage = make_montage(process())
    cv2.imshow("Lecture 7 - planar stitching", montage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
