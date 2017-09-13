n,d=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
if sum(a)%n==0:
    x=sum(a)/n
    for i in range(n):
        if a[i]>x:
            cnt+=(a[i]-x)
    print(int(cnt))
else:
    print("-1")