import socket

port = 8888
isRunning = False;

def start():
    server = socket.socket()
    server.bind(('',port))

    print("Starting Server on port",port)

    server.listen(5)
    print("Server listening")
    
    isRunning = True
    
    while isRunning:
        client, address = server.accept()
        print("New connection from",address)
        client.close()

def stop():
    isRunning = False
    print("Server stoped")

start()
