from itertools import permutations

def print_permutations(string):
    
    for perm in permutations(string):
        print(''.join(perm))

input = input("Введите : ")
print_permutations(input)