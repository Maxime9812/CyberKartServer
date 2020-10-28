from ClientHandle import *
from Server import *
from Server import Server
from threading import Thread


class Client:
    def __init__(self, socket, onDisconnect):
        self.socket = socket
        self.packetHandler = {2, ClientHandle._instance.change_direction}
        self.bufferSize = 1024
        self.isConnected = True
        self.thread = Thread(target=self.handlePacket, args=())
        self.thread.start()
        self.onDisconnect = onDisconnect

    def handlePacket(self):
        while self.isConnected:
            try:
                data = Server._instance.client.recv(self.bufferSize)

                if not data:
                    Server._instance.searchClient()

                packet_size = len(data)
                if packet_size >= 8:
                    [size, idPacket] = struct.unpack('ii', data[0:8])
                    packet = data[8:size]
                    self.packetHandler[idPacket](packet)

            except socket.timeout:
                self.disconnect()

    def disconnect(self):
        self.isConnected = False
        self.onDisconnect()
