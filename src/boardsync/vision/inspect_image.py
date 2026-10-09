from pathlib import Path

import cv2


CAPTURE_DIR = Path("data/captures")


def get_latest_capture() -> Path:
    captures = sorted(CAPTURE_DIR.glob("board_*.jpg"))

    if not captures:
        raise FileNotFoundError("No BoardSync captures found.")

    return captures[-1]


def inspect_image(image_path: Path) -> None:
    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    height, width, channels = image.shape

    print(f"Image: {image_path}")
    print(f"Width: {width}px")
    print(f"Height: {height}px")
    print(f"Channels: {channels}")
    print(f"Shape: {image.shape}")


if __name__ == "__main__":
    latest = get_latest_capture()
    inspect_image(latest)
