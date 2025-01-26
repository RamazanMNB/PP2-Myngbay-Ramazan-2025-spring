#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)