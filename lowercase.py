a=list(map(str,input().split(" ")))
print(a)
a=[x.upper() for x in a]
print(a)
a1=[]
for i in a:
    a1.append(list(i))
print(a1)
for i in range(len(a1)):
    for j in range(1,len(a[i]),2):
        a1[i][j]=a1[i][j].lower()
print(a1)
m=[]
for i in range(len(a1)):
    m.append("".join(str(x) for x in a1[i]))
print(m)
print(" ".join(str(x) for x in m))