n=int(input())
m=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split(" "))))
b=[]
k,x=m-1,0
for _ in range(m):
    c=[0]*n
    for i in range(n):
        c[i]=a[i][k]
    b.append(c)
    x=x+1
    k=k-1
for i in range(len(b)):
    print(" ".join(str(x) for x in b[i]))
""""to rotate a matrix in 90 deg anti-clockwise direction"""