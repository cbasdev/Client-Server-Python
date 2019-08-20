import zmq 


context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")

tam = 1024*1024*10

filename = "myfile.txt"


with open (filename, "rb") as f:
    while True:
        contents = f.read(tam)
        if not contents:
            break
        else:
            s.send_multipart([sha256.decode(), contents])
            #f.seek(tam)
            m = s.recv()

print (m)
#sha1sum file.format
#head -c 250M </dev/urandom > myfile.txt
#ifconfig192.168.0.15