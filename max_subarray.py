a=list(map(int,input().split()))
p,s=0,0
for i in range(0,len(a)):
    s=max(a[i],s+a[i])
    p=max(p,s)
print(p)