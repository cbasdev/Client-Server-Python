import zmq
import json
#Crear un contexto para interactuar con el cliente

context = zmq.Context()
socketClient = context.socket(zmq.REP)
socketClient.bind("tcp://*:5555")

catalogo = {
    "Placebo":"tcp://localhost:5556",
    "Metallica":"tcp://localhost:5557",
}

def buscarServer(artista):
    return catalogo[artista]

while True:
    nameSong, artista = socketClient.recv_multipart()
    socketClient.send_string("Buscando cancion")
    serverLink = buscarServer(artista.decode())
    
    #Crear un contexto para interactuar con el servidor

    socketServer = context.socket(zmq.REQ)
    socketServer.connect(str(serverLink))
    socketServer.send_multipart([nameSong, artista])
    m = socketServer.recv()

print("Esto no debería aparecer")


