import zmq
import json
import hashlib

tam = 1024*1024*10

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

catalogo = {
    "Radiohead":{
        "No Surprises" : "Radiohead/NoSurprises.wav",
        "Creep" : "Radiohead/Creep.wav",
        "Exit Music" : "Radiohead/ExitMusic.wav"
    },
    "Interpol":{
        "Obstacle 1": "Interpol/Obstacle1.wav",
        "Obstacle 2": "Interpol/Obstacle2.wav",
        "Obstacle 3": "Interpol/Obstacle3.wav"
    }
}

#Leemos el Archivo para enviar al server

def sendFile(filename):
    with open(fileSong, "rb") as f:
        while True:
            contents = f.read(tam)
            if not contents:
                break
            else:
                socket.send_multipart([contents])
                print (contents)
                m = socket.recv()



#Buscar la cancion en el Catalogo
def buscarSong(nameSong, artista):
    artistaD = artista.decode()
    nameSongD = nameSong.decode()
    fileSong = catalogo[artistaD][nameSongD]
    return fileSong

while True:
    nameSong, artista = socket.recv_multipart()
    fileSong = buscarSong(nameSong, artista)
    #socket.send_string("Buscando")
    sendFile(fileSong)
   # print (hashlib.fileSong())

    #print (nameSong, artista)

print ("Esto no debería aparecer")