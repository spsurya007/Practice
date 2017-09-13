import sys
a=input().strip()
x=list(a)
j=1
while (x!=(sorted(x,reverse=True))):
    x=[]
    i=0
    while (i+j<=len(a)):
        x.append(a[i:i+j])
        i=i+j
    j=j+1
x=list(map(int,x))
print(x)
for i in range(len(x)-1):
    if (x[i]-x[i+1]!=1):
        print(x[i+1]+1)
        break
