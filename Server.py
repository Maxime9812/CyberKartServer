import socket

class Server:
    def __init__(self, port, maxConnection):
      self.port = port
      self.maxConnection = maxConnection
      self.client = None
    
    def start(self):
        self.socket = socket.socket()
        self.socket.bind(('',self.port))

        print("Starting Server on port",self.port)

        self.socket.listen(self.maxConnection)
        print("Server listening")
        
        self.isRunning = True

    def stop(self):
        self.isRunning = False
        print("Server stoped")

    def searchClient(self):
        print("Search new client")
        self.client = None
        while self.client is None:
            newClient, address = self.socket.accept()
            self.client = newClient
            print("New connection from",address)
