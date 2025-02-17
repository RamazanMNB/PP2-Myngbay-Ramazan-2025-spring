def even_numbers(n):
    
    for num in range(0, n + 1, 2):
        yield num

n = int(input("number: "))


print(",".join(str(num) for num in even_numbers(n)))
