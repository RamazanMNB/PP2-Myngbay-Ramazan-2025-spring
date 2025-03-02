mylist=['kbtu','muit','kazgasa']
filename="input.txt"
with open(filename, "w", encoding="utf-8") as file:
    for i in mylist:
        file.write(i)