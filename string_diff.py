n=int(input())
x=[]
for i in range(n):
    x.append(list(input().strip()))
y=[]
for i in x:
    y.append(list(set(i)))
z=set(y[0]).intersection(set(y[1]))
if n>2:
    for i in range(2,len(y)):
        z=z.intersection(set(y[i]))
a=[]
for i in y:
    a.append(list(set(i)-z))
b=[]
for i in range(len(a)):
    for j in a[i]:
        b.append(j)
print("".join(str(c) for c in b))
