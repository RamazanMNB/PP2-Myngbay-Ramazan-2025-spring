import os

files = os.listdir(".")  
dirlist=[]
filelist=[]
for i in files:
    if os.path.isdir(i):
        dirlist.append(i)
    if os.path.isfile(i):
        filelist.append(i)
print(f"Directories-{dirlist}")
print(f"Files-{filelist}")
print(f"All list-{files}")


