"""Read, save, reload, and compare the image captured in exercise 02."""

from pathlib import Path

import cv2
import numpy as np

from labs.common import make_montage

LAB = Path(__file__).resolve().parents[1]
INPUT = LAB / "outputs" / "camera_frame.png"
OUTPUT = LAB / "outputs"


def image_round_trip(input_path: Path, output_directory: Path) -> list[tuple[str, np.ndarray]]:
    """Save PNG/JPEG copies and return four labelled uint8 BGR image panels.

    Read input_path and create output_directory if needed. Write still_copy.png
    and still_quality_35.jpg (JPEG quality 35), reload both, and print PNG pixel
    equality, both file sizes in bytes, and mean absolute JPEG channel error.
    Return, in order: Original BGR, PNG reload, JPEG reload, JPEG error x8.
    The last panel is absolute JPEG error amplified eightfold and clipped to
    0..255. All panels have the input image's shape. Reject failed reads/writes.
    """
    frame = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
    if frame is None:
        raise FileNotFoundError(
            f"Could not read {input_path}. Run ex02 and press S to save a camera frame."
        )

    output_directory.mkdir(parents=True, exist_ok=True)
    png_path = output_directory / "still_copy.png"
    jpeg_path = output_directory / "still_quality_35.jpg"
    if not cv2.imwrite(str(png_path), frame):
        raise RuntimeError("Could not write PNG")
    if not cv2.imwrite(str(jpeg_path), frame, [cv2.IMWRITE_JPEG_QUALITY, 35]):
        raise RuntimeError("Could not write JPEG")

    png = cv2.imread(str(png_path), cv2.IMREAD_COLOR)
    jpeg = cv2.imread(str(jpeg_path), cv2.IMREAD_COLOR)
    if png is None or jpeg is None:
        raise RuntimeError("Could not reload an output image")

    difference = cv2.absdiff(frame, jpeg)
    amplified = np.clip(difference.astype(np.int16) * 8, 0, 255).astype(np.uint8)
    pixel = frame[frame.shape[0] // 2, frame.shape[1] // 2]
    print(f"shape={frame.shape}, dtype={frame.dtype}, centre BGR pixel={pixel.tolist()}")
    print(f"PNG exact: {np.array_equal(frame, png)}, bytes={png_path.stat().st_size}")
    print(f"JPEG mean error: {difference.mean():.3f}, bytes={jpeg_path.stat().st_size}")
    return [
        ("Original BGR", frame),
        ("PNG reload", png),
        ("JPEG reload", jpeg),
        ("JPEG error x8", amplified),
    ]


def main() -> None:
    try:
        cv2.imshow("Lecture 3 - image I/O", make_montage(image_round_trip(INPUT, OUTPUT)))
        cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
