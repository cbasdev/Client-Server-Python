import zmq
import json

tam = 1024*1024*10
# Crear un contexto global para la comunicación

context = zmq.Context()

# Crear un contexto para interactuar con el Cliente

socketClient = context.socket(zmq.REP)
socketClient.bind("tcp://*:5558")

# Leer Archivo y enviar al Cliente
def sendFile(filename):
    print (filename)
    with open(filename, "rb") as f:
        contents = f.read()
      #  print (contents)
        socketClient.send_multipart([contents])
        #m = socketClient.recv()
while True:
    nameSong = socketClient.recv_string()
    nameSong = nameSong + ".wav"
    #print (nameSong)
    sendFile(nameSong)
    #socketClient.send_string(nameSong)