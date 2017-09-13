import math

n,m,k=map(int,input().split())
a=[int(x) for x in input().split()]
for i in range(m-1,n):
    if a[i]<=k and a[i]!=0:
        flag=i
for j in reversed(range(0,m,-1)):
    if a[j]<=k and a[i]!=0:
        flag1=j
else:
        flag1=flag
x=min(flag,flag1)
z=abs(x-(m-1))*10
print(z,flag,flag1)