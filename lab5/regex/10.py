

import re

with open(r"input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  

for line in lines:
    line = line.strip() 
    x = re.sub(r'(?<!^)([A-Z])', r'_\1', line).lower()
    print(x)
