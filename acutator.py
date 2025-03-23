@classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            thread = threading.Thread(target=cls._instance.start_detection, daemon=True)
            thread.start()
        return cls._instance

    def run(self, angle, throttle):
        global _detector_instance
        #detector_thread = threading.Thread(target=detector.start_detection, daemon=True)
        #detector_thread.start()
        #detector = RoboDetector.get_instance()
        #logging.info("acuator logging test")
        if _detector_instance is None:
            #logging.info("ndent")
            _detector_instance = RoboDetector()
            thread = threading.Thread(target=_detector_instance.start_detection, daemon=True)
            thread.start()
        else:
            logging.info(" ")
            #blank
        de = _detector_instance
        while de.is_robot_detected():
            logger.info("object detected")
            self.v.set_servo((0 * self.steering_scale) + self.steering_offset)
            self.v.set_duty_cycle(0*self.percent)
        self.v.set_servo((angle * self.steering_scale) + self.steering_offset)
        self.v.set_duty_cycle(throttle*self.percent)
        logger.info("object not detected")
        #if de.is_robot_detected():
            #self.v.set_servo((angle * self.steering_scale) + self.steering_offset)
            #self.v.set_duty_cycle(0 * self.percent)
            #logger.info("is")
        #else:
            #self.v.set_servo((angle * self.steering_scale) + self.steering_offset)
            #self.v.set_duty_cycle(throttle * self.percent)
            #logger.info("not")
