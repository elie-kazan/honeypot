from cmd import Cmd
import os
import logging

logging.basicConfig(filename='shell.log',level=logging.DEBUG)



class MyShell(Cmd):
    cwd = os.getcwd()
    prompt = cwd + '> '
    



    def do_exit(self,inp):
        print("exiting")
        logging.info("exiting")
        
        

        return True
    
    def do_cd(self,s):
        print("changing directory to " , s)
        logging.info("changing directory to " + s)
        os.chdir(s)
        self.cwd = os.getcwd()
        self.prompt = self.cwd + '> '
    

    def do_rm(self,s):
        print("deleting " , s)
        logging.info("deleting " + s)
        os.remove(s)

    def do_ls(self,s):
        files = os.listdir('.')
        for i in files:
            print(i)
        logging.info("listing files")

    def do_pwd(self,s):
        print(os.getcwd())
        logging.info("printing current working directory")

    def do_mkdir(self,s):
        os.mkdir(s)
        logging.info("making directory " + s)
    
    def do_rmdir(self,s):
        os.rmdir(s)
        logging.info("removing directory " + s)

    
    def do_touch(self,s):
        f = open(s,'w')
        f.close()
        logging.info("touching " + s)
    
    def do_cat(self,s):
        f = open(s,'r')
        print(f.read())
        f.close()
        logging.info("peaking into " + s)
    
    def do_cp(self,s):
        print("copying " , s)
        os.system("cp " + s)
        logging.info("copying " + s)
    
    def do_mv(self,s):
        print("moving " , s)
        os.system("mv " + s)
        logging.info("moving " + s)
    
    def do_chmod(self,s):
        print("changing mode of " , s)
        os.system("chmod " + s)
        logging.info("changing permissions of " + s)
    
    def do_chown(self,s):
        print("changing owner of " , s)
        os.system("chown " + s)
        logging.info("changing owner of " + s)
    
    def do_chgrp(self,s):
        print("changing group of " , s)
        os.system("chgrp " + s)
        logging.info("changing group of " + s)
    
    def do_find(self,s):
        print("finding " , s)
        os.system("find " + s)
        logging.info("finding " + s)
    
    def do_grep(self,s):
        print("grep " , s)
        os.system("grep " + s)
        logging.info("grep " + s)
    
    def do_sed(self,s):
        print("sed " , s)
        os.system("sed " + s)
        logging.info("sed " + s)

    
    


if __name__== '__main__':
    MyShell().cmdloop()
