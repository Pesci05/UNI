"""Core: detect several lines and circles in one global voting step."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 0
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]


def process(frame: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width)
    top, left = (height - side) // 2, (width - side) // 2
    card = frame[top:top + side, left:left + side]
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)

    gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Every non-zero pixel casts one vote for each line passing through it.
    # A thick filled stroke would let many slightly shifted or tilted lines
    # collect enough votes, so one stroke would return several duplicate segments.
    # Canny turns each stroke into two thin boundaries that vote for few lines.
    # Blurring the binary mask first smooths its staircase boundaries for Canny.
    blurred_mask = cv2.blur(mask, (7, 7))
    edges = cv2.Canny(blurred_mask, 45, 120)
    lines = cv2.HoughLinesP(edges, 
                            rho=1,  # distance resolution of the accumulator in pixels
                            theta=np.pi / 180,  # angular resolution of the accumulator in radians
                            threshold=max(1, round(0.10 * side)),  # minimum number of votes (intersections in Hough space) to detect a line
                            minLineLength=round(0.15 * side),  # minimum length of a line (in pixels) that will be accepted
                            maxLineGap=round(0.10 * side))  # maximum allowed gap between line segments to treat them as a single line

    # with method=cv2.HOUGH_GRADIENT, the function computes canny inside, so it is better to provide a blurred version
    # of the mask
    circles = cv2.HoughCircles(
        blurred_mask, 
        method=cv2.HOUGH_GRADIENT, 
        dp=1.2,  # inverse ratio of the accumulator resolution to the image resolution
        minDist=0.25 * side,  # minimum distance between the centers of detected circles
        param1=127,  # higher Canny threshold (the lower one is half of it)
        # each Canny edge pixel votes for possible centres along its gradient direction;
        # param2 is the minimum number of votes a centre needs. Lower it to accept
        # incomplete circles, raise it to reject weak or false ones.
        param2=max(12, round(0.05 * side)),
        minRadius=round(0.10 * side),  # minimum radius of circles to detect
        maxRadius=round(0.15 * side),  # maximum radius of circles to detect
    )

    overlay = card.copy()
    if lines is not None:
        for x1, y1, x2, y2 in lines.reshape(-1, 4):
            cv2.line(overlay, (x1, y1), (x2, y2), (0, 170, 0), 2)
    if circles is not None:
        for x, y, radius in np.rint(circles[0]).astype(int):
            cv2.circle(overlay, (x, y), radius, (0, 120, 255), 3)

    line_count = 0 if lines is None else len(lines)
    circle_count = 0 if circles is None else len(circles[0])
    label = f"Hough: {line_count} segments, {circle_count} circles"
    
    return [("Full camera frame: crop in green", full_view),
            ("Camera card", card),
            ("Segmented ink", mask),
            ("Canny boundary votes", edges),
            (label, overlay)]


def main() -> None:
    print("Fill the green square with the six-shape card. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 6 - Hough voting",
                           make_montage(process(frame), columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
