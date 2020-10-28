from Direction import Direction
from Motor import Motor
from Camera import Camera


class Kart:
    _instance = None

    def __init__(self, onCameraRead):
        if Kart._instance is None:
            Kart._instance = self

        self.direction = Direction()
        self.motor = Motor()
        self.camera = Camera(onCameraRead)
        self.camera.start()

    def turn(self, angle):
        self.direction.changeRotation(angle)

    def move(self, speed):
        if speed > 0:
            self.motor.forward()
        else:
            self.motor.stop()
