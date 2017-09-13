import itertools
a=list(map(int,input().split(" ")))
m=[]
for a,b,c in list(itertools.combinations(a,3)):
    if a+b+c==0:
        s=[a,b,c]
        s.sort()
        if s not in m:
            m.append(s)
if len(m)>0:
    m.sort()
    for i in range(len(m)):
        print(" ".join(str(x) for x in m[i]))
else:print("None")