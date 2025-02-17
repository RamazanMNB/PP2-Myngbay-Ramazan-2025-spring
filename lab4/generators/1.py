def square_generator(N):
    for num in range(1, N + 1):
        yield num ** 2 


N = 5
gen = square_generator(N)

for square in gen:
    print(square)
