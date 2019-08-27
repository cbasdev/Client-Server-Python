import zmq
import json
import hashlib
#Crear un contexto para interactuar con el cliente

context = zmq.Context()
socketClient = context.socket(zmq.REP)
socketClient.bind("tcp://*:5555")

catalogo = {
    "Radiohead":"tcp://localhost:5556",
    "Muse":"tcp://localhost:5557",
}

dictionar = {
    "onemoresong":[
        "p1", "p2", "p3"
    ]
}
def buscarServer(artista):
    return catalogo[artista]


#Leemos el Archivo para enviar al cliente





while True:
    nameSong, artista = socketClient.recv_multipart()
    #socketClient.send_string("Buscando cancion")
    serverLink = buscarServer(artista.decode())
    
    #Crear un contexto para interactuar con el servidor

    socketServer = context.socket(zmq.REQ)
    socketServer.connect(str(serverLink))
    socketServer.send_multipart([nameSong, artista])

    m = socketServer.recv()
    print (m)
    if not m:
        break
    else:
        socketClient.send_multipart([m])
        m2 = socketClient.recv()
    #sendFile(m)
    #socketClient.send_multipart([m])
    
    
    # = socketClient.recv()
    #print (r)

print("Esto no debería aparecer")


