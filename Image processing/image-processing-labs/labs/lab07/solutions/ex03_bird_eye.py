"""Core: rectify one physical plane from four visible point pairs."""

from pathlib import Path

import cv2
import numpy as np

from labs.common import make_montage

LAB = Path(__file__).resolve().parents[1]
ASSETS = LAB / "assets"

# Corresponding corners are listed clockwise from top-left. Keeping the table
# here makes point ordering visible and gives students one small array to edit.
SOURCE_POINTS = np.float32(
    [
        [125, 90],  # top-left in the perspective image
        [735, 40],  # top-right
        [780, 470],  # bottom-right
        [60, 430],  # bottom-left
    ]
)
# The 8:5 target must match the plane's real aspect ratio, or the result is stretched.
DESTINATION_POINTS = np.float32(
    [
        [0, 0],
        [799, 0],
        [799, 499],
        [0, 499],
    ]
)


def rectify(frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Four pairs give exactly the 8 unknowns: no redundancy, so one bad point goes unnoticed.
    homography = cv2.getPerspectiveTransform(SOURCE_POINTS, DESTINATION_POINTS)
    rectified = cv2.warpPerspective(frame, homography, (800, 500))
    return rectified, homography


def process(frame: np.ndarray):
    rectified, homography = rectify(frame)
    annotated = frame.copy()
    # Numbered points make the ordering visible, which is how swaps are spotted.
    for index, point in enumerate(SOURCE_POINTS.astype(int), 1):
        cv2.circle(annotated, tuple(point), 8, (0, 80, 255), -1)
        cv2.putText(
            annotated,
            str(index),
            tuple(point + [10, -10]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 80, 255),
            2,
            cv2.LINE_AA,
        )
    print("H=\n", homography)
    return [("Four source points, clockwise", annotated), ("Bird's-eye result", rectified)]


def main() -> None:
    frame = cv2.imread(ASSETS / "planar_perspective.png")
    montage = make_montage(process(frame))
    cv2.imshow("Lecture 7 - bird's-eye homography", montage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
