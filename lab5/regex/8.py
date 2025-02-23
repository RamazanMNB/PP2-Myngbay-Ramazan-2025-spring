
import re

with open(r"input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  

for line in lines:
    line = line.strip() 
    x = re.split(r'(?=[A-Z])', line)
    print(x)
