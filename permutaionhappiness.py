from itertools import permutations
n,k=map(int,input().split(" "))
c=list(permutations(range(1,n+1),n))
q=[]
for i in range(len(c)):
    count=0
    if (c[i][0]<c[i][1]):
        count+=1
    if ((c[i][1]<c[i][2]) or (c[i][0]>c[i][1])):
        count+=1
    if ((c[i][2]<c[i][1])):
        count+=1
    q.append(count)
d=q.count(k)
print(d)