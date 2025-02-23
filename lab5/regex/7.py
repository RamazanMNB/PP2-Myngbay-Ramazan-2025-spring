import re

with open(r"input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  

for line in lines:
    line = line.strip() 
    x = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), line)
    print(x)
