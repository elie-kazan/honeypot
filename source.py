import socket
import paramiko 
import logging 

logging.basicConfig(filename='myapp.log', level=logging.INFO)

s = socket.socket()
print("Socket successfully created ")
logging.info("Socket successfully created ")

port = 12345

s.bind(('',port))
print("Socket binded to %s" %(port))

s.listen(5)
print("socket is listening")



while True:

    c,addr = s.accept()
    print('Got a connection from ', addr)

    c.send('Thank you for connection'.encode())

    c.close()

    break




