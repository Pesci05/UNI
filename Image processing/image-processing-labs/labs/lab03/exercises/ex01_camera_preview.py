"""Run the camera preview, debug a frame, and add your own explanatory comments."""

import cv2

CAMERA_ID = 6


def main() -> None:
    camera = cv2.VideoCapture(CAMERA_ID)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera {CAMERA_ID}")

    print(f"Backend: {camera.getBackendName()}")
    print("Press Q in the image window to quit.")
    try:
        while True:
            ok, frame = camera.read()
            if not ok or frame is None:
                raise RuntimeError("Camera read failed")
            cv2.imshow("Camera preview", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
