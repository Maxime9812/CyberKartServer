from Server import *
import struct
from Kart import *
import threading
import time
import picamera
import io

server = Server(8888,1)
server.start()
bufferSize = 1024
tickPerSec = 2

threadLock = threading.Lock()

def change_direction(packet):
    [x,y] = struct.unpack('ff', packet)
    x = convert_range(x,-1,1,0,180)
    kart.move(y)
    kart.turn(x)

packetHandler = {2: change_direction,}


def convert_range(value, old_min, old_max, new_min, new_max):
    return ( (value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min


class StreamingOutput (object):
   def __init__(self):
      self.frame = None
      self.buffer = io.BytesIO()
      self.condition = threading.Condition()

   def write(self,buf):
      if buf.startswith(b'\xff\xd8'):
        self.buffer.truncate()
        with self.condition:
            self.frame = self.buffer.getvalue()
            self.condition.notify_all()
        self.buffer.seek(0)
      return self.buffer.write(buf)


def clientHandle():
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
   
def cameraSend():
    while server.isRunning:
        if server.client is not None:
            try:
            
                with picamera.PiCamera(resolution='640x480',framerate=30) as camera:
                    output = StreamingOutput()

                    camera.start_recording(output,format='mjpeg')
                    while server.client is not None:
                        with output.condition:
                            output.condition.wait()
                            frame = output.frame
                            packet = io.BytesIO()
                            packetToSend = io.BytesIO()
                            
                            packet.write(struct.pack('i',2))
                            packet.write(struct.pack('i',len(frame)))
                            packet.write(frame)
                            
                            packetToSend.write(struct.pack('i',len(packet.getvalue())))
                            packetToSend.write(packet.getvalue())
                            
                            print(server.client.send(packetToSend.getvalue()))
        
            except socket.timeout:
                server.client = None
            

kart = Kart()
camera = threading.Thread(target=cameraSend,args=())
camera.start()


clientHandle()







