import os, shutil
source = input("Enter the source folder: ")
destination = input("Enter the destination folder: ")

source = source + "/"
destination = destination + "/"

files = os.listdir(source)

for file1 in files:
    copy = shutil.copy((source + file1), destination)


