import cv2
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("camera_detection.log"),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

detected_object = []


# File to share detection state - this will be read by vehicle.py or actuator.py
#DETECTION_STATE_FILE = '/tmp/object_detection_state.txt'


# Initialize the state file with "0" (no detection)
#with open(DETECTION_STATE_FILE, 'w') as f:
   # f.write('0')
   # logging.info(f"Initialized detection state file: {DETECTION_STATE_FILE}")


class RoboDetector:
        def __init__(self):
                self.robot_detected = False


        def detection_callback(self, packet):
                detections = packet.detections
                #logging.info("detection runs")
                if len(detections) > 0:
                        self.robot_detected = True
                else:
                        self.robot_detected = False

        def start_detection(self):
                with OakCamera(usb_speed='usb2') as oak:
                        color = oak.create_camera('color')
                        model_config = {
                                'source': 'roboflow', # Specify that we are downloading the model from Roboflow
                                'model': 'obstacles-x27hl-0iswo/1', #beverage-containers-3atxb/2',
                                'key': 'ggQjV8UgC2yOO6wzm1eg'   #'1U5Gwe0TRsIWmwPVGmvv' # FAKE Private API key, replace with your own!
                        }
                        logging.info("test")
                        nn = oak.create_nn(model_config, color)
                        logging.info(f"Neural network type: {type(nn)}")
                        logging.info(f"Neural network methods: {str(dir(nn))[:200]}...")
                        oak.callback(nn, self.detection_callback)
                        logging.info("add callback")
                        #oak.visualize(nn, fps=True)
                        logging.info("running visualization")
                        oak.start(blocking=True)
        def is_robot_detected(self):
                return self.robot_detected
