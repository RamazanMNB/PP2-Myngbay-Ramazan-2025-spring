import os


path = input("Enter the path: ")


if os.path.exists(path):
    print("The path exists.")
    
    
    filename = os.path.basename(path)
    print("Filename:", filename)


    directory = os.path.dirname(path)
    print("Directory:", directory)

else:
    print("The path does not exist.")
