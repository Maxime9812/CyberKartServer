from Server import *
from ServerSend import *
from ClientHandle import *
from Kart import *

# Initialize Server
server = Server(8888)
ServerSend()
ClientHandle()

server.start()

# Initialize Kart
kart = Kart()







