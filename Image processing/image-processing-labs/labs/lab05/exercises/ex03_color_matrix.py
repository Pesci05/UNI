"""Core: sample eight chart patches and fit an empirical RGB correction."""

import cv2
import numpy as np

from labs.common import camera_frames, make_montage

CAMERA_ID = 0
REQUESTS = [("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
            ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0),
            # manually distort color settings to simulate an issue to correct
            ("auto white balance", cv2.CAP_PROP_AUTO_WB, 0.0),
            ("white balance temperature", cv2.CAP_PROP_WB_TEMPERATURE, 6500.0),
            ("hue", cv2.CAP_PROP_HUE, 40.0)]

# Row 1 colours, then the first and last neutral patches in row 4.
PATCHES = [(0, column) for column in range(6)] + [(3, 0), (3, 5)]
REFERENCE_RGB = np.array([
    [0.721569, 0.219608, 0.200000], [0.239216, 0.549020, 0.250980],
    [0.180392, 0.321569, 0.721569], [0.721569, 0.600000, 0.141176],
    [0.580392, 0.219608, 0.619608], [0.160784, 0.619608, 0.639216],
    [0.780392, 0.780392, 0.780392], [0.109804, 0.109804, 0.109804],
], np.float64)


def process(frame: np.ndarray):
    height, width = frame.shape[:2]
    side = min(height, width)
    top, left = (height - side) // 2, (width - side) // 2
    crop = frame[top:top + side, left:left + side]

    # sample fixed patch centres while the cardboard fills the square crop
    rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB).astype(np.float64) / 255.0
    radius = max(3, round(0.015 * side))
    positions = []
    measured = []
    # first patch centre and grid spacing as fractions of the card side
    for row, column in PATCHES:
        x = round(side * (0.125 + column * 0.15))
        y = round(side * (0.275 + row * 0.15))
        positions.append((x, y))
        patch = rgb[y - radius:y + radius + 1, x - radius:x + radius + 1]
        measured.append(patch.mean(axis=(0, 1)))
    measured = np.asarray(measured)

    # fit measured @ matrix to the eight reference RGB pairs (np.linalg.lstsq is numerically more stable)
    # TODO 1: compute the 3 x 3 matrix that minimizes |measured @ matrix - REFERENCE_RGB|^2
    matrix, _, _, _ = np.linalg.lstsq(measured, REFERENCE_RGB, rcond=None)

    # apply the correction to every pixel, clipping to the displayable RGB range
    # TODO 2: multiply every RGB pixel of rgb by matrix and clip to [0, 1] as corrected_rgb
    corrected_rgb = np.clip(rgb.astype(np.float32) @ matrix, 0.0, 1.0)
    corrected = cv2.cvtColor(np.rint(corrected_rgb * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    residual = np.abs(measured @ matrix - REFERENCE_RGB).mean()

    # visualization and debugging
    full_view = frame.copy()
    cv2.rectangle(full_view, (left, top), (left + side - 1, top + side - 1), (0, 200, 0), 3)
    annotated = crop.copy()
    for index, (x, y) in enumerate(positions, 1):
        cv2.circle(annotated, (x, y), radius, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(annotated, str(index), (x - 10, y - radius - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (20, 20, 20), 2)
    # one column per pair; rows: measured, corrected, reference
    swatches = np.stack([measured, np.clip(measured @ matrix, 0.0, 1.0), REFERENCE_RGB])
    swatches = np.repeat(np.repeat(swatches, 60, axis=0), 60, axis=1)
    swatches = cv2.cvtColor(np.rint(swatches * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

    return [("Full camera frame: crop in green", full_view),
            ("Eight live RGB sample positions", annotated),
            ("Measured / corrected / reference", swatches),
            (f"Normalized chart; fit residual {residual:.3f}", corrected)]


def main() -> None:
    print("Fill the green square with the colour chart under fixed light. Press Q to quit.")
    try:
        with camera_frames(CAMERA_ID, REQUESTS) as frames:
            for frame in frames:
                cv2.imshow("Lecture 5 - empirical RGB normalization", make_montage(process(frame), columns=2, panel_width=360))
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
