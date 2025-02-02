def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num=(input())
 
nums = list(map(int, num.strip().split()))

prime = filter(lambda x:is_prime(x),nums)

print(list(prime))