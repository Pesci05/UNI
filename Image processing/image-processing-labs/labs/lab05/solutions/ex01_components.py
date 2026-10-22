"""Core: label and filter the six dark objects on a printed card."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 0
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]

COLOURS = [(220, 90, 60), (70, 180, 70), (60, 100, 220),
           (200, 80, 180), (40, 190, 210), (180, 150, 40)]


def process(frame: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width)
    top, left = (height - side) // 2, (width - side) // 2
    crop = frame[top:top + side, left:left + side]
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)

    # find components by labeling the dark objects in the binary image
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, ink = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    count, labels, stats, centroids = cv2.connectedComponentsWithStats(ink, connectivity=8)

    # filter away small components based on area
    minimum_area = max(500, round(side * side * 0.0025))
    accepted = [label for label in range(1, count)
                if stats[label, cv2.CC_STAT_AREA] >= minimum_area]
    
    # visualization and debugging
    coloured = np.zeros_like(crop)
    annotated = crop.copy()
    for index, label in enumerate(accepted):
        colour = COLOURS[index % len(COLOURS)]
        coloured[labels == label] = colour
        x, y, box_width, box_height, _ = stats[label]
        cv2.rectangle(annotated, (x, y), (x + box_width, y + box_height), colour, 3)
        cv2.putText(annotated, str(index + 1), (x, max(20, y - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, colour, 2)

    return [("Full camera frame: crop in green", full_view),
            ("Camera card", crop),
            ("Binary objects", ink),
            ("Component labels", coloured),
            (f"Accepted objects: {len(accepted)} / 6", annotated)]


def main() -> None:
    print("Fill the green square with the shape card. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 5 - components", make_montage(process(frame), columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
