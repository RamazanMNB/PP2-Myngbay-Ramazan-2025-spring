total = {}
def insert(item):
    if item in total:
        total[item] += 1
    else:
        total[item] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))