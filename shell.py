from cmd import Cmd
import os

class MyShell(Cmd):
    cwd = str(os.getcwd())

    prompt = cwd + '> '

    def do_exit(self,inp):
        print("exiting")
        return True
    def do_cd(self,s):
        cwd = os.chdir(s)

    cwd = str(os.getcwd())    




if __name__== '__main__':
    MyShell().cmdloop()
