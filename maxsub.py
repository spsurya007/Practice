from itertools import combinations
x1,k=map(int,input().split(" "))
a=[]
for line in range(4):
    a.append(int(input()))
c=list(combinations(a,k))
q = []
for i in range(len(c)):
    for j in range(len(c[i])-(k-1)):
        g = (c[i][j]&c[i][j+1])
        if (k==2):
            g&=c[i][k-1]
    q.append(g)
x=max(q)
y=q.count(x)
print(x)
print(y)