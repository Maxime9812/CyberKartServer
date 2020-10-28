import socket
from Client import *


class Server:
    _instance = None

    def __init__(self, port):
        if Server._instance is None:
            Server._instance = self

        self.port = port
        self.maxConnection = 1
        self.client = None

    def start(self):
        self.socket = socket.socket()
        self.socket.bind(('', self.port))

        print("Starting Server on port", self.port)

        self.socket.listen(self.maxConnection)
        print("Server listening")

        self.isRunning = True

        while self.isRunning:
            if self.client is None:
                self.searchClient()

    def stop(self):
        self.isRunning = False
        print("Server stopped")

    def searchClient(self):
        print("Search new client")
        self.client = None
        while self.client is None:
            newClient, address = self.socket.accept()
            self.client = Client(newClient, self.onClientDisconnected)
            print("New connection from", address)

    def onClientDisconnected(self):
        self.client = None
