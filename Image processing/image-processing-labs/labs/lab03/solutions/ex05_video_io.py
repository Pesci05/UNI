"""Read the video recorded in exercise 04, write a mirrored copy, and replay it."""

from math import isfinite
from pathlib import Path

import cv2

LAB = Path(__file__).resolve().parents[1]
INPUT = LAB / "outputs" / "camera_clip.avi"
OUTPUT = LAB / "outputs" / "motion_mirrored.avi"


def open_video(path: Path) -> tuple[cv2.VideoCapture, float, tuple[int, int]]:
    if not path.is_file():
        raise FileNotFoundError(f"Missing {path}. Run ex04 to record camera_clip.avi first.")
    video = cv2.VideoCapture(str(path))
    try:
        if not video.isOpened():
            raise RuntimeError(f"Could not open {path}. Record a new clip with ex04.")
        fps = float(video.get(cv2.CAP_PROP_FPS))
        width = float(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = float(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if not all(isfinite(value) and value > 0 for value in (fps, width, height)):
            raise ValueError(f"Invalid FPS or dimensions in {path}. Record a new clip with ex04.")
        if not width.is_integer() or not height.is_integer():
            raise ValueError(f"Invalid frame dimensions in {path}. Record a new clip with ex04.")
        return video, fps, (int(width), int(height))
    except Exception:
        video.release()
        raise


def mirror_video(input_path: Path, output_path: Path) -> dict[str, float]:
    video, fps, size = open_video(input_path)
    writer = None
    count = 0
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        writer = cv2.VideoWriter(
            str(output_path), cv2.VideoWriter_fourcc(*"MJPG"), fps, size
        )
        if not writer.isOpened():
            raise RuntimeError(f"Could not open VideoWriter for {output_path}; check MJPG support.")
        while True:
            ok, frame = video.read()
            if not ok:
                break
            if frame is None or frame.shape[:2] != (size[1], size[0]):
                raise RuntimeError(f"Invalid frame in {input_path}. Record a new clip with ex04.")
            writer.write(cv2.flip(frame, 1))
            count += 1
    finally:
        if writer is not None:
            writer.release()
        video.release()
    if count == 0:
        raise RuntimeError(f"No readable frames in {input_path}. Record a new clip with ex04.")

    metadata = {"fps": fps, "frames": float(count), "duration": count / fps}
    print(metadata)
    return metadata


def replay(path: Path) -> None:
    video, fps, _ = open_video(path)
    try:
        while True:
            ok, frame = video.read()
            if not ok:
                break
            cv2.imshow("Mirrored video - Q to stop", frame)
            if cv2.waitKey(max(1, round(1000 / fps))) & 0xFF == ord("q"):
                break
    finally:
        video.release()
        cv2.destroyAllWindows()


def main() -> None:
    mirror_video(INPUT, OUTPUT)
    replay(OUTPUT)


if __name__ == "__main__":
    main()
