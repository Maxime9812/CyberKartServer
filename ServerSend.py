from Server import *

class ServerSend:
    _instance = None

    def __init__(self):
        if ServerSend._instance == None:
            ServerSend._instance = self
    def sendToClient(self,packet):
        if Server._instance.client is not None:
           Server._instance.client.socket.send(packet.getvalue())

    def SendCameraData(self, frame):
        packet = io.BytesIO()
        packetToSend = io.BytesIO()

        packet.write(struct.pack('i', 2))
        packet.write(struct.pack('i', len(frame)))
        packet.write(frame)

        packetToSend.write(struct.pack('i', len(packet.getvalue())))
        packetToSend.write(packet.getvalue())
        self.sendToClient(packetToSend)