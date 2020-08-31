from time import time, sleep
from picamera import PiCamera
import io
import threading

class Camera:
    thread = None
    frame = None
    last_access = 0

    def initialize(self):
        if Camera.thread is None:
            Camera.thread = threading.Thread(target=self.__thread__)
            Camera.thread.start()
        while self.frame is None:
            pass

    def get_frame(self):
        Camera.last_access = time()
        self.initialize()
        return self.frame

    @classmethod
    def __thread__(cls):
        with PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.rotation = 180
            sleep(2)
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, "jpeg", use_video_port=True):
                stream.seek(0)
                cls.frame = stream.read()
                stream.seek(0)
                stream.truncate()
                if time() - cls.last_access > 10:
                    break
            cls.thread = None
