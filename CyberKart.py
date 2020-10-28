from Server import *
from ServerSend import *
from ClientHandle import *
from Kart import *

ClientHandle()
ServerSend()

packetHandle = {2: ClientHandle._instance.change_direction}


def handlerClient(idPacket, packet):
    packetHandle[idPacket](packet)


def OnCameraRead(frame):
    ServerSend._instance.SendCameraData(frame)

# Initialize Kart
kart = Kart(OnCameraRead)

# Initialize Server
server = Server(8889, handlerClient)
server.start()
