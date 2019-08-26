import zmq
import json
#Crear un contexto para interactuar con el cliente

contextClient = zmq.Context()
socketClient = contextClient.socket(zmq.REP)
socketClient.bind("tcp://*:5555")


while True:
    nameSong, artista = socketClient.recv_multipart()
    socketClient.send_string("Buscando cancion")

print("Esto no debería aparecer")

#Crear un contexto para interactuar con el servidor

contextServer = zmq.Context()
socketServer = contextServer(zmq.REQ)
socketServer.connect("tcp://localhost:5556")

catalogo = {
    "placebo": "tcp:(//*5556)",
    "metallica":"tcp:(//*5557)",
}