n=int(input())
a=[]
for i in range(n):
    a.append(input().strip())
y=int(input())
x=input().strip()
v=""
m=x
b=[]
b.append(x)
while m!=v:
    for i in range(n):
        if x[-1]==a[i][0]:
            b.append(a[i])
            x=a[i]
            v=a[i]
            break
b.pop()
print(b)
if y > len(b):
    y-=len(b)
    print(b[y-1])
else:
    print(b[y-1])