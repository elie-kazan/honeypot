from cmd import Cmd
import os
import logging

# get current time
import time

current_time = time.strftime("%H:%M:%S")

filename="shell.log_"+current_time

logging.basicConfig(filename=filename,level=logging.DEBUG,format='%(asctime)s %(message)s')



class MyShell(Cmd):

    cwd = os.getcwd()
    prompt = cwd + '> '

    # display a banner
    def preloop(self):
        print("Welcome to my shell")
        logging.info("Welcome to my shell")
    
    def do_exit(self,inp):
        print("exiting")
        logging.info("exiting")
        return True
    
    def do_cd(self,s):
        # catch the exception
        try:
            print("changing directory to " , s)
            logging.info("changing directory to " + s)
            os.chdir(s)
            self.cwd = os.getcwd()
            self.prompt = self.cwd + '> '
        except Exception as e:
            print(e)
            logging.info(e)
        

    def do_rm(self,s):
        try:
            print("deleting " , s)
            logging.info("deleting " + s)
            os.remove(s)
        except Exception as e:
            print(e)
            logging.info(e)
        

    def do_ls(self,s):
        try:
            files = os.listdir('.')
            for i in files:
                print(i)
            logging.info("listing files")
        except Exception as e:
            print(e)
            logging.info(e)
        

    def do_pwd(self,s):
        try:
            print(os.getcwd())
            logging.info("printing current working directory")
        except Exception as e:
            print(e)
            logging.info(e)

        

    def do_mkdir(self,s):
        try:
            os.mkdir(s)
            logging.info("creating directory " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_rmdir(self,s):
        try:
            print("deleting directory " , s)
            os.rmdir(s)
            logging.info("deleting directory " + s)
        except Exception as e:
            print(e)
            logging.info(e)

    
    def do_touch(self,s):
        try:
            f = open(s,'w')
            f.close()
            logging.info("touching " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_cat(self,s):
        try:
            f = open(s,'r')
            print(f.read())
            f.close()
            logging.info("peaking into " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_cp(self,s):
        try:
            print("copying " , s)
            os.system("cp " + s)
            logging.info("copying " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_mv(self,s):
        try:

            print("moving " , s)
            os.system("mv " + s)
            logging.info("moving " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_chmod(self,s):
        try:
            print("changing mode of " , s)
            os.system("chmod " + s)
            logging.info("changing permissions of " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_chown(self,s):
        try:
            print("changing owner of " , s)
            os.system("chown " + s)
            logging.info("changing owner of " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_chgrp(self,s):
        try:
            print("changing group of " , s)
            os.system("chgrp " + s)
            logging.info("changing group of " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_find(self,s):
        try:
            print("finding " , s)
            os.system("find " + s)
            logging.info("finding " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_grep(self,s):
        try:
            print("grep " , s)
            os.system("grep " + s)
            logging.info("grep " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    def do_sed(self,s):
        try:
            print("sed " , s)
            os.system("sed " + s)
            logging.info("sed " + s)
        except Exception as e:
            print(e)
            logging.info(e)
    
    # in case of any error
    def default(self,s):
        
        
        logging.info("executing " + s)
    
    def emptyline(self):
        pass
    
    


if __name__== '__main__':    
    MyShell().cmdloop()

