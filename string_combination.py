a=input().strip()
b=input().strip()
c=""
x=0
for i in range(len(a)):
    if a[i:] in b:
        c=a[i:]
        x=i
        break
print(c)
print((a[0:x]+c+b[len(c):]))