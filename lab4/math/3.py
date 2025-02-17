import math
def arr(sid,len,ct):
    print(int(((sid*len**2)/4)*ct))
p=math.pi
sides=int(input("Number of sides:"))
a=int(input("Length:"))
x=p/sides
cot=1/math.tan(x)
arr(sides,a,cot)