from Direction import Direction
from Motor import Motor

class Kart:
    def __init__(self):
        self.direction = Direction()
        self.motor = Motor()
    
    def turn(self, angle):
        self.direction.changeRotation(angle)
    
    def move(self, speed):
        if speed > 0:
            self.motor.forward()
        else:
            self.motor.stop()
