a=5
b="apples"
print(a,b)
a=10
b=15
print(a+b)
a="hello"
b="world"
print(a+" "+b)




x="kbtu"
def func():
    print("Best universe is " + x)
func()



x="iitu"
def func():
    global x
    x="kbtu"
func()
print("best universe is "+x)