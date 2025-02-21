import re

with open(r"input.txt", "r", encoding="utf-8") as file:

    lines = file.readlines()  

for line in lines:

    x = re.sub("\W",":",line)
    print(x)
    
    