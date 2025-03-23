import logging
import os
import time
from camerausb import RoboDetector

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("camera_detection.log"),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

detector = RoboDetector()
logging.info("'{detector'}")

#separate thread
import threading


detector_thread = threading.Thread(target=detector.start_detection, daemon=True)
detector_thread.start()


try:
        while True:
                if detector.is_robot_detected():
                        logging.info("robo detected")
                else:
                        logging.info("no robo detected")
                time.sleep(1)
except KeyboardInterrupt:
        print("stopping detection...")



