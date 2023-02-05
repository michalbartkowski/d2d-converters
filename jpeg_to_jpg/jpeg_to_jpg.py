import os
import shutil

def make_dir(name):
    # make a folder for the images
    try:
        os.makedirs(str(name))
        print(f'Made directory: ./{name}')
    except:
        pass



current_dir = os.getcwd()
directory = os.fsencode(current_dir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpeg"):
        print(f'File ___ {filename} ___ renamed to ___ {filename[:-4]}.jpg')
        os.rename(filename, filename[:-4]+'jpg')