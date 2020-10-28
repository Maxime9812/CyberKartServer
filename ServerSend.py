from Server import *

class ServerSend:
    _instance = None

    def __init__(self):
        if ServerSend._instance == None:
            ServerSend._instance = self
