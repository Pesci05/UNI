"""Core: open the course webcam, preview frames, and close it safely."""

import cv2

CAMERA_ID = 2


def main() -> None:
    # Open the selected camera through an available OpenCV video backend.
    camera = cv2.VideoCapture(CAMERA_ID)
    # Construction alone does not guarantee that the device opened successfully.
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(f"Could not open camera {CAMERA_ID}")

    # The backend connects OpenCV to the operating system's camera interface.
    print(f"Backend: {camera.getBackendName()}")
    print("Press Q in the image window to quit.")
    try:
        while True:
            # read() returns a success flag and the next decoded image array.
            ok, frame = camera.read()
            # Check the result before using the image; a disconnected camera can fail.
            if not ok or frame is None:
                raise RuntimeError("Camera read failed")
            # Show the BGR image in a named window, reusing it on the next iteration.
            cv2.imshow("Camera preview", frame)
            # waitKey processes window events and briefly waits for a key.
            # Mask to the low byte and compare with the character code for lowercase q.
            # Focus the image window when pressing the key; this is not an FPS setting.
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        # Always give the camera back, including when reading raises an error.
        camera.release()
        # Close OpenCV's windows after the loop finishes.
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Run only when this file is executed, never merely when it is imported.
    main()
