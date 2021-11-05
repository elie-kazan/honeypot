from cmd import Cmd
import os

class MyShell(Cmd):
    cwd = os.getcwd()
    prompt = cwd + '> '

    def do_exit(self,inp):
        print("exiting")
        return True
    def do_cd(self,s):
        os.chdir(s)

    def do_rm(self,s):
        print("deleting " , s)
        os.remove(s)

    def do_ls(self,s):
        files = os.listdir('.')
        for i in files:
            print(i)

    def do_pwd(self,s):
        print(os.getcwd())

    def do_mkdir(self,s):
        os.mkdir(s)
    
    def do_rmdir(self,s):
        os.rmdir(s)
    
    def do_touch(self,s):
        f = open(s,'w')
        f.close()
    
    def do_cat(self,s):
        f = open(s,'r')
        print(f.read())
        f.close()
    
    def do_cp(self,s):
        print("copying " , s)
        os.system("cp " + s)
    
    def do_mv(self,s):
        print("moving " , s)
        os.system("mv " + s)
    
    def do_chmod(self,s):
        print("changing mode of " , s)
        os.system("chmod " + s)
    
    def do_chown(self,s):
        print("changing owner of " , s)
        os.system("chown " + s)
    
    def do_chgrp(self,s):
        print("changing group of " , s)
        os.system("chgrp " + s)
    
    def do_find(self,s):
        print("finding " , s)
        os.system("find " + s)
    
    def do_grep(self,s):
        print("grep " , s)
        os.system("grep " + s)
    
    def do_sed(self,s):
        print("sed " , s)
        os.system("sed " + s)
    
    





if __name__== '__main__':
    MyShell().cmdloop()
