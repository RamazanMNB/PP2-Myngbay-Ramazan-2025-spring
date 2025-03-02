import os
path="C:\\Users\\Рамазан\\.ssh\\ramazan"

if  os.path.exists(path):
    print("You have this directory")
else:
    print("You havent got")
    if  os.access(path, os.R_OK):
        print("You can read")
    else :
        print("you cant read")
    if  os.access(path, os.W_OK):
        print("You can write")
    else:
        print("You cant write")
    if  os.access(path, os.W_OK):
        print("You can check")
    else :
        print("You cant check")
