# a python script to steal data 

# get the current directory
import os


current_dir = os.getcwd()

list_of_files = os.listdir(current_dir)



for i in list_of_files:
    if i == "Github":
        print("found github")
        
       