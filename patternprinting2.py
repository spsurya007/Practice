a=str(input())
a=a[(len(a)//2):]+a[0:(len(a)//2)]
q,p,y=[],[],[]
for i in range(len(a)-1,-1,-1):
    q.append("*"*i)
for i in range(1,len(a)+1):
    p.append(a[0:i])
for i in range(max(len(p),len(q))):
    y.append(q[i]+p[i])
for i in y:
    print("".join(str(x) for x in i))
