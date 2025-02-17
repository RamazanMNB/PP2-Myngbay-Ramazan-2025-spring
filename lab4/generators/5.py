def countdown(n):
    
    for num in range(n, -1, -1): 
        yield num

n = int(input("Enter a number: "))


print(f"Countdown from {n} to 0:")
for num in countdown(n):
    print(num)
