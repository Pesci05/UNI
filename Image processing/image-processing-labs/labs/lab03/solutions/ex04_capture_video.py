"""Capture enough webcam frames for about five seconds of nominal playback."""

from math import isfinite
from pathlib import Path

import cv2

CAMERA_ID = 2
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "camera_clip.avi"


def main() -> None:
    camera = cv2.VideoCapture(CAMERA_ID)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera {CAMERA_ID}")
    ok, frame = camera.read()
    if not ok or frame is None:
        camera.release()
        raise RuntimeError("Could not read the first frame")

    height, width = frame.shape[:2]
    fps = float(camera.get(cv2.CAP_PROP_FPS))
    if not isfinite(fps) or fps <= 0:
        fps = 30.0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(
        str(OUTPUT), cv2.VideoWriter_fourcc(*"MJPG"), fps, (width, height)
    )
    if not writer.isOpened():
        camera.release()
        raise RuntimeError("Could not open VideoWriter")

    try:
        for _ in range(round(5 * fps)):
            ok, frame = camera.read()
            if not ok or frame is None:
                raise RuntimeError("Camera read failed")
            writer.write(frame)
            cv2.imshow("Recording", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        writer.release()
        camera.release()
        cv2.destroyAllWindows()
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
