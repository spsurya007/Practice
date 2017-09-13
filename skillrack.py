import math

x,y=input().split(" ")
x=int(x)
y=int(y)
def skill():
    z=[int(c) for c in input().split() ]
    z.sort(reverse=True)
    c=z[0:y]
    v=sum(c)
    print(v)
skill()