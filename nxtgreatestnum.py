ip=str(input())
a=list(ip)
q=[]
for j in range(len(a)-1,0,-1):
    if q ==[]:
        for i in range(j,-1,-1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
                q=i
                break
            else:continue
print(a)
x=a[:q+1]
y=a[q+1:]
y.sort()
t="".join(str(m) for m in x+y)
print(t)