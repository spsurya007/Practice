n=int(input())
a=list(map(int,input().split(" ")))
c=[]
for i in range(n):
    if a[i]>0 and a[i]%2!=0:
        c.append(a[i])
    elif a[i]%2==0:
        c.append(int(str(a[i])[::-1]))
print(sum(c))