import zmq 
import hashlib

context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")

tam = 1024*1024*10

s.send_multipart([b"This picture", b"Placebo"])
m = s.recv()

print (m)

'''
#print (nombreArchivo)

#print (m)
#sha1sum file.format
#head -c 250M </dev/urandom > myfile.txt
#ifconfig192.168.0.15

'''