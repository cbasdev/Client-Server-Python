import zmq

context = zmq.Context()
s = context.socket(zmq.REP)

s.bind("tcp://*:5555")

def store(message, filename):
    with open(filename, "wb") as f:
        f.write(message)


while True:
    name, m = socket.recv_multipart()
    store(m, "f-" + str(name.decode("utf-8")))
    socket.send_string("Mensaje enviado")

print ("Esto no debería aparecer")