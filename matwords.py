n=int(input())
a=[]
for i in range(n):
    a.append(list(map(str,input())))
x=list(input())
y=list(input())
y.remove(y[0])
def alter(a):
    q = []
    for i in range(n):
        for j in a[i]:
            if j == '*':
                q.append((i, a[i].index(j)))
            else:
                continue
    q=list(set(q))
    q.sort()
    for (i, j) in q:
        if len(x)>0:
            a[i][j] = x[0]
            x.remove(x[0])
            alter(a)
        else:
            a[i][j]=y[1]
            y.remove(y[1])
            alter(a)
alter(a)