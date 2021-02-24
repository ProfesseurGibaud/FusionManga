import os
import shutil

path = os.path.join(os.getcwd(),"Fusion")
for i in os.listdir():
    if os.path.isdir(i):
        os.chdir(i)
        for j in os.listdir():
            newname = i +" "+ j
            shutil.copyfile(j,os.path.join(path,newname))
        os.chdir("..")