from datetime import datetime
from pathlib import Path
from picamera2 import Picamera2
import time


OUTPUT_DIR = Path("data/captures")


def capture_image() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = OUTPUT_DIR / f"board_{timestamp}.jpg"

    camera = Picamera2()
    camera.start()

    time.sleep(2)

    camera.capture_file(str(output_path))
    camera.stop()

    print(f"Image saved to {output_path}")
    return output_path


if __name__ == "__main__":
    capture_image()