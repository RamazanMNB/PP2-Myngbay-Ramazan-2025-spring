def solve(numheads, numlegs):
    kurs=(numlegs-4*numheads)/-2
    krol=numheads-kurs
    print(int(kurs),int(krol))
a=int(input())
b=int(input())
solve(a,b)
