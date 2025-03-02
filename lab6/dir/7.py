with open("input.txt", "r", encoding="utf-8") as i:
    content = i.read()  

with open("input2.txt", "w", encoding="utf-8") as change:
    change.write(content) 

print("Exelent")