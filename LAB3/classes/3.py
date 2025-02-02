class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    
Shape=shape()
print(Shape.area())

Rectangle=rectangle(2,5)
print(Rectangle.area())
    