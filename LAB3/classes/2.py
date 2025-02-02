class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class square(shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length ** 2


Shape=shape()
print(Shape.area()) #по умолчанию

Square = square(5)
print(Square.area()) 
