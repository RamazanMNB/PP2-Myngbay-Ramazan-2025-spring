import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)

    def move(self, x2, y2):
        self.x = x2
        self.y = y2

    def dist(self, other_point):
        dis = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return dis


print("Enter the first point")
a, b = int(input("First Coordinates: ")), int(input("Second Coordinates: "))
pnt1 = Point(a, b)


print("Enter the second point")
c, d = int(input("First Coordinates: ")), int(input("Second Coordinates: "))
pnt2 = Point(c, d)


pnt1.show()
pnt2.show()


print("Change the first point")
f, h = int(input("First Coordinates: ")), int(input("Second Coordinates: "))
pnt1.move(f, h)

# print change coordinates
pnt1.show()

# distance
distance = pnt1.dist(pnt2)
print(distance)
