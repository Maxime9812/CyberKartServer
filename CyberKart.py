from Server import *
from Kart import *

server = Server(8888,1)
server.start()
server.searchClient()

kart = Kart()
kart.turn(20)
