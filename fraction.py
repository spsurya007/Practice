import sys
n=int(input())
a=[]
for i in range(1,n+1):
    if i==2 or i==1:
        a.append(i)
    elif 2**(i-1)%i==1:
        a.append(i)
for i in range(len(a)):
    for j in range(i):
        if a[i]+a[j]==n:
            print(min(a[i],a[j]),max(a[i],a[j]))
            sys.exit()

