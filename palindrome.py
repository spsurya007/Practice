n=int(input())
q=[]
for i in range(n):
    a=list(str(input().strip()))
    q.append(a)
print(q)
m=[]
for i in range(len(q)):
    m+=q[i]
print(m)
m.sort()
print(m)
c,d=[],[]
for i in m:
    if (m.count(i) == 2):
        if i not in d:
            d.append(i)
    elif m.count(i)>2:
        if i not in d:
            d.append(i)
        c.append(i)
    else:
        c.append(i)
print(c)
print(d)
f=[]
for i in d:
    if m.count(i) in range(2,100,2):
        for k in range(m.count(i)//2):
            f.append(i)
    elif m.count(i)>2 :
        f.append(i)
print(f)
print("".join(x for x in f)+c[0]+"".join(x for x in f[::-1]))
