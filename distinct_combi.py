import itertools
n,m=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
x=list(set(itertools.combinations(a,2)))
print(x)
c=[]
for i,j in x:
    if i>j:
        i,j=j,i
        c.append((i,j))
    else:
        c.append((i,j))
c=list(set(c))
print(c)
cnt=0
for i,j in c:
    if i+j==m:
        cnt+=1
if m in a:
    cnt+=1
print(cnt)