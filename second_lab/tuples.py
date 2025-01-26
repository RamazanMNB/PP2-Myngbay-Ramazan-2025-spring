#1
fruits = ("apple", "banana", "cherry")
print(len(fruits))


fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#2
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)

fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#3
mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

