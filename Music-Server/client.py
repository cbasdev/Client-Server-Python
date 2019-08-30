import zmq 
import hashlib
import json
import pygame

# Contexto Global para la comunicacion

context = zmq.Context()

# Socket para Preguntar por el catalogo al proxy

socketProxy = context.socket(zmq.REQ)
socketProxy.connect("tcp://localhost:5555")

socketProxy.send_multipart([b"No Surprises", b"Radiohead"])
serversEncode = socketProxy.recv()
servers = json.loads(serversEncode.decode())
#print (serers["NoSurprices-pt1"])
#print (servers)
# Socket para Buscar canción en el server

song = b""

for server in servers:
    socketServer = context.socket(zmq.REQ)
    #socketServer.connect(server)
    socketServer.connect(servers[server])
    #print(servers[server])
    socketServer.send_string(server)
    #print(server)
    part = socketServer.recv()
    print(type(part))
    song = song + part

#print(song)

#Reproduccion de cancion
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
#song = bytes(song)
print(song)
sound = pygame.mixer.Sound(buffer= song)
while True:
    sound.play()    
