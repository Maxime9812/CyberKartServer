from Direction import Direction

class kart:
    def __init__(self):
        self.direction = Direction()
    
    def turn(self, angle):
        self.direction.changeRotation(angle)
