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






if __name__== '__main__':
    MyShell().cmdloop()
