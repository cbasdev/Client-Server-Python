import zmq 
import hashlib

context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")

tam = 1024*1024*10

filename = "myfile.txt"

#EN esta primera lectura se calcula el Sha256 para todo el archivo
with open (filename, "rb") as f:
    sha256 = hashlib.sha256()
    while True:
        contents = f.read(tam)
        if not contents:
            break
        sha256.update(contents)

#Nombre del archivo
nombreArchivo = sha256.hexdigest().encode()

#AHora leemos el archivo y enviamos al servidor
with open(filename, "rb") as f:
    while True:
        contents = f.read(tam)
        if not contents:
            break
        else:
            s.send_multipart([nombreArchivo,contents])
            m = s.recv()

#print (nombreArchivo)

#print (m)
#sha1sum file.format
#head -c 250M </dev/urandom > myfile.txt
#ifconfig192.168.0.15