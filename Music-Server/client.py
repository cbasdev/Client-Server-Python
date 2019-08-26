import zmq 
import hashlib
import pygame





context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://localhost:5555")

tam = 1024*1024*10

s.send_multipart([b"No Surprises", b"Radiohead"])
m = s.recv()
print (m)



pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

sound = pygame.mixer.Sound(buffer=m)
while True:
    sound.play()    