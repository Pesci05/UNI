"""Implement image round trips using the frame captured in exercise 02."""

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
    raise NotImplementedError("Implement image_round_trip using the README and documentation.")


def main() -> None:
    try:
        cv2.imshow("Lecture 3 - image I/O", make_montage(image_round_trip(INPUT, OUTPUT)))
        cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
