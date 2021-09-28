import sockets
import paramiko
import os

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




