import sockets
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

    def log(self,action,date):
        """Log the action with the date of the action in the log.txt file """
        log_file = open("./log.txt", "a")
        log_file.write("\n")
        log_file.write(str(action) + " " + str(date) + " " + str(datetime.now()))
        log_file.close()

    
    





