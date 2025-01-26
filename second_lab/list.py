#1
mylist = ['apple', 'banana', 'cherry']
print(mylist[1])

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
#2
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])
#3
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])
#4
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
#6
for x in ['apple', 'banana', 'cherry']:
  print(x)


mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
#7
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']

fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#8
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
