name=input("Hello! What is your name?")

print("Well, "+name+" , I am thinking of a number between 1 and 20.")
print("Take a guess.")

import random 

a=random.randint(1,20) 
count=1
while True: 
    b=input() 
    if b=="q": 
        break 
    b=int(b) 
    if b<a: 
        print("Your guess is too low.") 
        print("Take a guess.") 
        count+=1
    elif b>a: 
        print ("Your guess is too high.") 
        print ("Take a guess.") 
        count+=1
    elif a==b: 
        print ("Good job, "+name+"! You guessed my number in "+str(count)+" guesses!") 
        break 