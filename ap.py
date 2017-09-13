f=list(map(int,input().split(" ")))
f.sort()
if all((i-j)==(j-k) for i,j,k in zip(f[:-2],f[1:-1],f[2:])):
        print("-1")
else:
    q=list(zip(f[:-2],f[1:-1],f[2:]))
    #print(q)
    a=[]
    for i,j,k in q:
        if (i-j)!=(j-k):
            a.append(i)
            a.append(j)
            a.append(k)
        elif (i-j)==(j-k):
            z=abs(i-j)
    #print(z)
    #print(a)
    b=list(set(a))
    print(b)
    d=[]
    for i in b:
        d.append(i%z)
    print(d)
    w=list(set(d))
    print(w)
    for i in w:
        if d.count(i)==1:
            k=i
    print(k)
    r=d.index(k)
    print(r)
    print(b[r])
