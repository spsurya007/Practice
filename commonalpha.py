n=int(input())
a=[]
for i in range(n):
    a.append(set(input()))
m=(set.intersection(*a))
m=list(m)
m.sort()
if len(m)>0:
    print("".join(str(x) for x in m))
else:print("-1")