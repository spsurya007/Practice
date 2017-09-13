n=int(input())
x=[]
for i in range(1,n+1):
    a=[]
    a.append(i)
    f=i
    for j in range(n,i,-1):
        f+=j
        a.append(f)
    x.append(a)
for i in range(len(x)):
    print(" ".join(str(j) for j in x[i]))
