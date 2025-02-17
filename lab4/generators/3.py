def divisible_by_3_and_4(n):
    
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("number: "))


print("3 and 4:", list(divisible_by_3_and_4(n)))
