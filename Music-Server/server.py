import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")


def buscarSong(nameSong, artista):
    print("buscar")

while True:
    nameSong, artista = socket.recv_multipart()
    buscarSong(nameSong, artista)
    socket.send_string("Buscando")

print ("Esto no debería aparecer")