import os
import shutil

path = input("Please Enter The path of the file: ")
files = os.listdir(path) # List of files - Obtaining a list of all the files in the dir

# Traversing through every file from files
# Splitting the filename and its extension
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:] # Removing the dot from the extension (.jpg), so it can be used as a dir name

    # If the extension directory exists, we move the file to it
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else: # Making new dir and moving the files into it
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
