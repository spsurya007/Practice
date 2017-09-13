n=int(input())
k=int(input())
l=[]
def fd(l,n):
    for i in range(0,len(l),n):
        if l[i]==1:
            l[i]=0
        else:l[i]=1
for i in range(n):
    l.append(1)
for i in range(2,n):
    fd(l,i)
if l[k]==1:
    print("open")
else:print("close")