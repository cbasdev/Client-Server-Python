import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

def store(message, filename):
    with open(filename, "ab") as f:
        f.write(message)


while True:
    sha256, m = socket.recv_multipart()
    store(m, sha256.decode())
    socket.send_string("Mensaje enviado")

print ("Esto no debería aparecer")