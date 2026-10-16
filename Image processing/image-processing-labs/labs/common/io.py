"""Small image, camera, and montage helpers provided to students."""

from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path
import sys

import cv2
import numpy as np

Panel = tuple[str, np.ndarray]
CameraRequest = tuple[str, int, float]


def load_bgr(path: str | Path) -> np.ndarray:
    """Load one colour image or raise a useful error."""

    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")
    return image


@contextmanager
def camera_frames(camera_id: int, requests: Sequence[CameraRequest] = ()) -> Iterator[Iterator[np.ndarray]]:
    """Yield frames, restore every requested property, and release the camera."""

    # on window, prefer DirectShow to avoid issues with color controls
    CAMERA_API = cv2.CAP_DSHOW if sys.platform == "win32" else cv2.CAP_ANY

    camera = cv2.VideoCapture(camera_id, CAMERA_API)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera {camera_id}")

    def frames() -> Iterator[np.ndarray]:
        while True:
            ok, frame = camera.read()
            if not ok or frame is None:
                raise RuntimeError(f"Could not read from camera {camera_id}")
            yield frame

    original = []
    try:
        # Read every original value before a request can affect another control.
        original = [(property_id, float(camera.get(property_id))) for _, property_id, _ in requests]

        # first we set all properties, then we read them again
        requests_res = []
        for label, property_id, value in requests:
            requests_res.append(bool(camera.set(property_id, value)))

        # print the results of the requests
        for (label, property_id, value), accepted in zip(requests, requests_res):
            print(f"{label}: requested={value}, set()={accepted}, actual={float(camera.get(property_id))}")

        yield frames()

    finally:
        try:
            # Restore manual controls before re-enabling automatic controls.
            for property_id, value in reversed(original):
                camera.set(property_id, value)
        finally:
            camera.release()


def _display_bgr(image: np.ndarray) -> np.ndarray:
    if image.ndim == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if image.ndim == 3 and image.shape[2] == 3:
        if image.dtype == np.uint8:
            return image
        maximum = 1.0 if float(np.nanmax(image)) <= 1.0 else 255.0
        return np.rint(np.clip(image, 0, maximum) * (255.0 / maximum)).astype(np.uint8)
    raise ValueError("Display panels must be grayscale or three-channel images")


def make_montage(
    panels: Sequence[Panel],
    *,
    columns: int = 2,
    panel_width: int = 480,
) -> np.ndarray:
    """Build one labelled BGR image from several result panels."""

    if not panels:
        raise ValueError("At least one panel is required")
    if columns < 1 or panel_width < 80:
        raise ValueError("Invalid montage dimensions")

    tiles = []
    for label, source in panels:
        image = _display_bgr(np.asarray(source))
        scale = panel_width / image.shape[1]
        resized = cv2.resize(
            image,
            (panel_width, max(1, round(image.shape[0] * scale))),
            interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR,
        )
        tile = cv2.copyMakeBorder(resized, 42, 8, 8, 8, cv2.BORDER_CONSTANT, value=(245,) * 3)
        font_scale = 0.72
        available_width = tile.shape[1] - 28
        text_width = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 2)[0][0]
        if text_width > available_width:
            font_scale *= available_width / text_width
        cv2.putText(
            tile,
            label,
            (14, 29),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (30, 30, 30),
            2,
            cv2.LINE_AA,
        )
        tiles.append(tile)

    rows = (len(tiles) + columns - 1) // columns
    cell_height = max(tile.shape[0] for tile in tiles)
    cell_width = max(tile.shape[1] for tile in tiles)
    canvas = np.full((rows * cell_height, columns * cell_width, 3), 225, np.uint8)
    for index, tile in enumerate(tiles):
        y = (index // columns) * cell_height
        x = (index % columns) * cell_width
        canvas[y : y + tile.shape[0], x : x + tile.shape[1]] = tile
    return canvas
