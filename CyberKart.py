from Server import *
import struct
from Kart import *




def change_direction(packet):
    [x,y] = struct.unpack('ff', packet)
    x = convert_range(x,-1,1,0,180)
    kart.move(y)
    kart.turn(x)

packetHandler = {2: change_direction,}


server = Server(8888,1)
server.start()
bufferSize = 1024;

def convert_range(value, old_min, old_max, new_min, new_max):
    return ( (value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

kart = Kart()
while server.isRunning:
    if server.client is not None:
        try:
            data = server.client.recv(bufferSize)
            
            if not data:
                server.searchClient()
                
            packet_size = len(data)
            if packet_size >= 8:
                [size,idPacket] = struct.unpack('ii', data[0:8])
                packet = data[8:size]
                packetHandler[idPacket](packet)
                    
        
        except socket.timeout:
            server.client = None
    else:
        server.searchClient()




