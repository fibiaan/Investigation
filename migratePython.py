from msilib.schema import Directory
import subprocess
from os import listdir
from os.path import isfile, isdir

def lookFolder(directory):
    parent = listdir(directory)
    for child in parent:
        parts = child.split(".")
        relative = directory + child
        if(parts[-1] == 'py' and isfile(relative)):
            print('is python file: ', relative)
            subprocess.call('2to3 -w ' + relative)
        elif (isdir(relative) and child != ".git"):
            print('is a directory ', relative)
            lookFolder(relative + '/')

lookFolder('C:/Users/fibia/AppData/Local/Programs/Python/Python310/lib/site-packages/meshtool/')


# subprocess.call(['ls'])