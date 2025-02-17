def squares(a, b):
    
    for num in range(a, b + 1):
        yield num ** 2 


a = int(input("start number : "))
b = int(input("end number : "))


print(f"Squares from {a} to {b}:")
for square in squares(a, b):
    print(square)
