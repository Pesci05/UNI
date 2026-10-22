"""Core: compare enclosing priors, fitted models, and polygonal structure."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 1
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]


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

    if len(accepted) != 6:
        return [("Full camera frame: crop in green", full_view),
                ("Camera card", crop),
                (f"Found {len(accepted)} shapes, expected 6", np.where(labels > 0, 255, 0).astype(np.uint8))]

    # sort from top to bottom, left to right
    # we need to sort because we assume a given shape (e.g. triangle) is in a given position (e.g. second row, 
    # second column). in this exercise, we are not predicting shapes, only fitting based on _prior_.
    accepted = sorted(accepted, key=lambda label: centroids[label, 1])  # sorted is NOT inplace
    accepted = sorted(accepted[:3], key=lambda label: centroids[label, 0]) + \
               sorted(accepted[3:], key=lambda label: centroids[label, 0])

    # prepare visualizations
    shape_view = crop.copy()
    polygon_view = crop.copy()

    # enclosing methods use every foreground pixel of each accepted component
    points = [cv2.findNonZero(np.where(labels == label, 255, 0).astype(np.uint8)) for label in accepted]
    
    # (1, 1): enclose upright rectangle (the minimum-area rectangle is axis aligned here)
    box = cv2.boxPoints(cv2.minAreaRect(points[0])).astype(np.int32)
    cv2.polylines(shape_view, [box], True, (0, 180, 0), 4, cv2.LINE_AA)

    # (1, 2): enclose rotated rectangle
    box = cv2.boxPoints(cv2.minAreaRect(points[1])).astype(np.int32)
    cv2.polylines(shape_view, [box], True, (0, 180, 0), 4, cv2.LINE_AA)

    # (1, 3): enclose circle
    center, radius = cv2.minEnclosingCircle(points[2])
    cv2.circle(shape_view, tuple(np.array(center).astype(int)), round(radius), (0, 120, 255), 4)

    # (2, 1): fit ellipse
    # for fitting and approximating, we need to work directly on contour points, we can do that through canny, 
    # findContours (or morphological gradient)
    ellipse_edges = cv2.Canny(np.where(labels == accepted[3], 255, 0).astype(np.uint8), 100, 200)
    ellipse_points = np.array(np.where(ellipse_edges)).T[:, [1, 0]]
    ellipse = cv2.fitEllipse(ellipse_points)
    cv2.ellipse(shape_view, ellipse, (210, 80, 180), 4, cv2.LINE_AA)

    # (2, 2): enclose triangle
    _, triangle = cv2.minEnclosingTriangle(points[4])
    cv2.polylines(shape_view, [triangle.astype(np.int32)], True, (40, 170, 220), 4)

    # (2, 3): enclose concave shape in its convex hull, which bridges the notch
    hull = cv2.convexHull(points[5])
    cv2.polylines(polygon_view, [hull], True, (0, 150, 255), 4, cv2.LINE_AA)

    # (2, 3): approximate the same shape with a polygon (prior: few straight sides)
    # different from the convex hull, this polygon approximation follows the actual edges, which is a _sorted_
    # collection of points. so we must extract them with findContours
    component = np.where(labels == accepted[5], 255, 0).astype(np.uint8)
    candidates, _ = cv2.findContours(component, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # epsilon is the largest allowed distance from the contour: 0 keeps every pixel step,
    # too large cuts the notch away
    epsilon = 0.01 * cv2.arcLength(candidates[0], True)
    polygon = cv2.approxPolyDP(candidates[0], epsilon, True)
    cv2.polylines(polygon_view, [polygon], True, (170, 70, 210), 4, cv2.LINE_AA)

    # finalize visualizations
    foreground = np.where(np.isin(labels, accepted), 255, 0).astype(np.uint8)

    return [("Full camera frame: crop in green", full_view),
            ("Camera card", crop),
            ("Foreground pixels for enclosing", foreground),
            ("Known priors: enclose or fit", shape_view),
            ("Orange convex hull / purple concave polygon", polygon_view)]


def main() -> None:
    print("Fill the green square with the shape card. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 5 - simple shape priors", make_montage(process(frame), columns=3, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
