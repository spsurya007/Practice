n=int(input())
a=[]
for i in range(n):
    a.append((input().split(" ")))
x=input()
y=0
for i in range(n):
    if a[i][0]==x:
        y=i
for i in range(y+1,n):
    print(a[i][1])