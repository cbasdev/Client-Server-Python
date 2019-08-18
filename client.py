import zmq 


ctx = zmq.Context()
s = ctx.socket(zmq.REQ)
s.connect("tcp://192.168.0.11   :5555")


filename = "amapolas2.jpg"


with open (filename, "rb") as f:
    contents = f.read()
    s.send_multipart([filename.encode("utf-8"), contents])
m = s.recv_string()

#sha1sum file.format
#head -c 250M </dev/urandom > myfile.txt
#ifconfig