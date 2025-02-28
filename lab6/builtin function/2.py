text=input()
countup=0
countlow=0
for i in text:
    if i.isupper():
        countup+=1
    if i.islower():
        countlow+=1
print(countup,countlow)