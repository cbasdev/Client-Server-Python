import zmq 


ctx = zmq.Context()
s = ctx.socket(zmq.REQ)
s.connect("tcp://192.168.17.35:5555")


filename = "SebastianVelez.txt"


with open (filename, "rb") as f:
    contents = f.read()
    s.send_multipart([filename.encode("utf-8"), contents])
m = s.recv_string()import zmq 
import json

ctx = zmq.Context()
s   = ctx.socket(zmq.REP)
#REP como voy a usar el socket "reply"
s.bind("tcp://*:5555")
# * elija interfaz red por defecto actual
#bind es un enlace
#tcp el protocolo a usarse

filename = "amapolas2.jpg"

with open ("amapolas2.jpg", "rb") as f:
    byte = 

#sha1sum 
#head -c 250M </dev/urandom > myfile.txt

while True:
    m = s.recv()
    imagen.write(m)
    print(" Mensaje Recibido",m ,type(m))
    s.send(b"guardado")

print("Esto no deberia aparecer")



print("Recibi: {}".format(m))