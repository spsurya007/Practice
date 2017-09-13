n=int(input())
s=0
for i in range(1,n+1):
   s+=i
q=list(range(s,0,-1))
a=[]
for i in range(0,n):
    m=[]
    k=i
    for j in range(n,i,-1):
        m.append(q[k])
        k+=j
    a.append(m)
for i in range(len(a)):
    print(" ".join(str(x) for x in a[i]))