def reverse(a):
    a= list.strip().split()
    a.reverse()
    for i in range(0,len(a)):
        print(a[i],end=" ") 



list=input()
reverse(list)



