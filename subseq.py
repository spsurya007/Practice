string=str(input().strip())
l=list(set(string))
print(l)
minima=9999
for i in range(len(string)):
    l2=[]+l[:]
    k=-1
    for j in range(i,len(string)):
        if string[j] in l2:
            l2.remove(string[j])
        if l2==[]:
            k=j
            break
    if k!=-1:
        temp=k-i
        if temp<minima:
            minima=temp
print(l2)
print(minima+1)