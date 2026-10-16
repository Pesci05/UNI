"""Extend the preview: discover property identifiers, request/read values, and save."""

from pathlib import Path

import cv2

CAMERA_ID = 6
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "camera_frame.png"
REQUESTS = [
    ("width", cv2.CAP_PROP_FRAME_WIDTH, 800.0),
    ("height", cv2.CAP_PROP_FRAME_HEIGHT, 600.0),
    ("fps", cv2.CAP_PROP_FPS, 30.0),
]


def request(camera: cv2.VideoCapture, name: str, property_id: int, value: float) -> float:
    if property_id is None:
        raise NotImplementedError(f"Find the OpenCV property identifier for {name}.")

    accepted = camera.set(property_id, value)
    actual = camera.get(property_id)

    print(f"{name}: requested={value}, set()={accepted}, actual={actual}")
    return actual


def main() -> None:
    camera = cv2.VideoCapture(CAMERA_ID)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera {CAMERA_ID}")
    print("Press S to save one frame, or Q to quit.")
    try:
        for name, property_id, value in REQUESTS:
            request(camera, name, property_id, value)
        while True:
            ok, frame = camera.read()
            if not ok or frame is None:
                raise RuntimeError("Camera read failed")
            cv2.imshow("Camera properties", frame)
            key = cv2.waitKey(1) & 0xFF
            # TODO: check if key pressed is "s" to save the frame; write frame to str(OUTPUT); check if successful.
            if key == ord("s"):
                print("Premuto il tatso s")
                path = Path("labs/lab03/outputs/camera_frame.png")
                path.parent.mkdir(parents=True,exist_ok=True)
                path.touch()
                print(f"cartella e file creati al percorso {path}")
                success = cv2.imwrite(str(OUTPUT),frame)
                print(OUTPUT)

                if success:
                    print(f"Immagine salvata in {OUTPUT}")
                else:
                    raise RuntimeError("Cannot save frame",frame)          

            if key == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
