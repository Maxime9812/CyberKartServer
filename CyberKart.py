from Server import *
#from Kart import *

server = Server(8888,1)
server.start()

while server.isRunning:
    if server.client is not None:
        try:
            data = server.client.recv(1024)
            if not data:
                server.searchClient()
            print("Packet :",data)
        except socket.timeout:
            server.client = None
    else:
        server.searchClient()
#kart = Kart()

