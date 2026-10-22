"""Optional: find printed symbols and expose rotation and scale sensitivity."""

from pathlib import Path

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

LAB = Path(__file__).resolve().parents[1]
ASSETS = LAB / "assets"
CAMERA_ID = 1
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0)]


def process(frame: np.ndarray, template: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width)
    top, left = (height - side) // 2, (width - side) // 2
    crop = frame[top:top + side, left:left + side]
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)

    # compare the crop with the supplied template at its fixed pixel size
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # TODO: compute scores, the mean-subtracted normalized correlation of template
    # at every position of gray
    raise NotImplementedError("Compute the template score map")

    # find local peaks in the template matching score map
    peaks = (scores >= 0.75) & (scores == cv2.dilate(scores, np.ones((15, 15), np.uint8)))
    locations = np.column_stack(np.nonzero(peaks))

    # visualization
    result = crop.copy()
    match_height, match_width = template.shape
    
    for y, x in locations:
        cv2.rectangle(result, (x, y), (x + match_width, y + match_height), (0, 170, 0), 3)
    
    heatmap = cv2.applyColorMap((np.clip(scores, 0, 1) * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
    
    return [("Full camera frame: crop in green", full_view),
            ("Printed template scene", crop),
            ("Template score map", heatmap),
            (f"Upright matches: {len(locations)}", result)]


def main() -> None:
    # load the template once, already sized for the expected 600 px camera crop
    template = cv2.imread(ASSETS / "template.png", cv2.IMREAD_GRAYSCALE)
    print("Fill the green square with the template scene. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 5 - template matching", make_montage(process(frame, template), columns=2, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
