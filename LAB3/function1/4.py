def filter_prime(a, b):
    for number in a:
        if number > 1:  
            count = 0
            for j in range(2, int(number ** 0.5) + 1):
                if number % j == 0:
                    count += 1
            if count == 0:  
                b.append(number)
    print(b)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = []
filter_prime(numbers, newlist)





