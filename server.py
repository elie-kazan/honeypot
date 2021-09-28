import socket
import paramiko
import os
from datetime import datetime

class Server(paramiko.ServerInterface):

    def __init__(self):
        print("Created a server ")
    
    def log_init(self):
        """ Creer un fichier log de type txt , et dans le cas ou il existe deja auccune action ne sera faite"""
        if(os.path.isfile("./log.txt")):
            pass
        else:
            log_file = open("./log.txt", "w")
            log_file.write('My first log')
            log_file.close()

    def log(self,action,date,client_addr=("","")):
        """Log the action with the date of the action in the log.txt file , prend le tuple client addr qui 
        est retourner par la method listen en tant que parametre optionnel """

        log_file = open("./log.txt", "a")
        log_file.write("\n")
        log_file.write(str(action) + " " + str(date) + " " + str(datetime.now()))
        log_file.close()

    def listen(self):
        """retourne le client et l'addr lors d'une connexion """

        host = "127.0.0.1"
        port = 3000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        print("Server started listenning ")
        sock.listen()
            
        client, addr = sock.accept()
        return (client, addr)                          

        

    





