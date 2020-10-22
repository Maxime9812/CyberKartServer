from Server import *
import struct
from Kart import *

server = Server(8888,1)
server.start()

def convert_range(value, old_min, old_max, new_min, new_max):
    return ( (value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

kart = Kart()
while server.isRunning:
    if server.client is not None:
        try:
            data = server.client.recv(1024)
            if not data:
                server.searchClient()
            
            [x,y] = struct.unpack('ff', data)
            
            print("x",convert_range(x,-1,1,0,180))
            print("y",convert_range(y,-1,1,0,180))
            kart.turn(convert_range(y,-1,1,0,180))
        
        except socket.timeout:
            server.client = None
    else:
        server.searchClient()

