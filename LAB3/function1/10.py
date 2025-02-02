def unique_elements(lst):
    list = []
    for item in lst:
        if item not in list:
            list.append(item)
    return list

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique = unique_elements(numbers)
print(unique)
