# from Kart import *
import struct
from ServerSend import *

def convert_range(value, old_min, old_max, new_min, new_max):
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min


class ClientHandle:
    _instance = None

    def __init__(self):
        if ClientHandle._instance is None:
            ClientHandle._instance = self

    def change_direction(self, packet):
        [x, y] = struct.unpack('ff', packet)
        x = convert_range(x, -1, 1, 0, 180)
        #Kart._instance.move(y)
        #Kart._instance.turn(x)
