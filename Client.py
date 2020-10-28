from threading import Thread
import struct


class Client:
    def __init__(self, socket, onDisconnect, onPacketReceived):
        self.socket = socket
        self.onPacketReceived = onPacketReceived
        self.bufferSize = 1024
        self.isConnected = True
        self.thread = Thread(target=self.handlePacket, args=())
        self.thread.start()
        self.onDisconnect = onDisconnect

    def handlePacket(self):
        while self.isConnected:
            try:
                data = self.socket.recv(self.bufferSize)

                if not data:
                    self.disconnect()

                packet_size = len(data)
                if packet_size >= 8:
                    [size, idPacket] = struct.unpack('ii', data[0:8])
                    packet = data[8:size]
                    self.onPacketReceived(idPacket, packet)

            except self.socket.timeout:
                self.disconnect()

    def disconnect(self):
        self.isConnected = False
        self.onDisconnect()
