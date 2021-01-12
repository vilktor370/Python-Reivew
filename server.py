#phone dial
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('vilktor.com',80))#actual connection

#HTTP Hyptertext Transfer Protocol
#bridge betweem server and browser

cmd="GET http://vilktor.com/ HTTP/1.0\n\n".encode()
mysock.send(cmd)
while True:
    data=mysock.recv(4000)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()