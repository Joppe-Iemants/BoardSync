from picamera2 import Picamera2
from pathlib import Path
import time


OUTPUT_DIR = Path("data/captures")


def capture_image():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    camera = Picamera2()
    camera.start()

    time.sleep(2)

    output_path = OUTPUT_DIR / "test_capture.jpg"
    camera.capture_file(str(output_path))

    camera.stop()

    print(f"Image saved to {output_path}")


if __name__ == "__main__":
    capture_image()
