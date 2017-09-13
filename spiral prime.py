"""n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().strip().split(" "))))
for i in range(len(a)):
    a[i].remove(len(a[i])-1)
    a[i].sort()
    print(a[i][-1])"""

"""import itertools
n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(list(map(int,input().strip().split(" "))))
print(a)
for i in a:
    cnt=0
    x1=list(itertools.combinations(i,2))
    print(x1)
    x=[]
    for f in x1:
        if 1<=f[0] and f[0]<f[1] and f[1]<=len(i):
            x.append(f)
    print(x)
    for j in x:
        if (j[0]|j[1])<=max(j[0],j[1]):
            cnt+=1
    print(cnt)"""

t=int(input())
x=[]
for i in range(t):
    z=[]
    n=int(input())
    for j in range(n):
        z.append(list(map(int,input().strip().split(" "))))
    x.append(z)
for f in x:
    xl, yl, xs, ys = -1, -1, 1000000001, 1000000001
    for i in f:
        if i[0] > xl:
            xl = i[0]
        elif i[1] > yl:
            yl = i[1]
        if i[0] < xs:
            xs = i[0]
        elif i[1] < ys:
            ys = i[1]
    print(max(abs(xl-xs),abs(yl-ys)))