import zmq
import json
import hashlib

# QUE ARCHIVOS TIENE CADA SERVIDOR

files = {
    "NoSurprises-pt1":"tcp://localhost:5556",
    "NoSurprises-pt2":"tcp://localhost:5557",
    "NoSurprises-pt3":"tcp://localhost:5558",
    "GreenEyes-pt1":"tcp://localhost:5558",
    "GreenEyes-pt2":"tcp://localhost:5557",
    "GreenEyes-pt3":"tcp://localhost:5558",

}

# QUE PARTES TIENE CADA CANCIÓN

parts = {
    "No Surprises":[
        "NoSurprises-pt1", "NoSurprises-pt2", "NoSurprises-pt3"
    ],
    "Green Eyes":[
        "GreenEyes-pt1","GreenEyes-pt2","GreenEyes-pt3"
    ]
}

# Crear un contexto global para la comunicación

context = zmq.Context()

# Crear un contexto para iteractuar con el cliente

socketClient = context.socket(zmq.REP)
socketClient.bind("tcp://*:5555")

# Funcion Para Buscar las partes de la cancion:

def searchPartsOfSong(song):
    partsOfSong = parts[song]
    return partsOfSong

# Funcion para Buscar los servidores de las Partes:

def searchServersOfSong(partsServer):
    serversOfSong = []
    for p in partsServer:
        serversOfSong.append(files[p])
    return serversOfSong

# Unir las dos listas

def relationItems(list1, list2):
    relationList = {}
    iterator = 0
    for item in list1:
        relationList.update ({item:list2[iterator]})
        iterator += 1      
    return relationList

# Recibir mensajes del Cliente

while True:
    nameSong, artista = socketClient.recv_multipart()
    partsOfSong = searchPartsOfSong(nameSong.decode())
    serversOfSong = searchServersOfSong(partsOfSong)
    relationList = relationItems(partsOfSong, serversOfSong)
    socketClient.send_json(relationList)

#Leemos el Archivo para enviar al clientes

'''
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
'''