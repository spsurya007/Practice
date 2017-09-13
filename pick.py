"""import itertools

N=int(input())
q=[]
for i in range(N):
    q.append([x for x in input().strip()])


def pick(x):
    m = itertools.permutations((x), 2)
    for l in m:
        if int(l[0] + l[1]) in range(65, 91):
            c.append(chr(int(l[0] + l[1])))


for l in q:
    c=[]
    pick(l)
    c=list(set(c))
    c.sort()
    print("".join(i for i in c))"""

import itertools
N=int(input())
s=[]
apl=[(6,5),(6,6),(6,7),(6,8),(6,9),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(9,0)]
for i in range(N):
    x=[int(ii) for ii in input().strip()]
    c=[]
    z=list(itertools.permutations(x,2))
    for i in apl:
        if i in z:
            c.append(chr(int(str(i[0])+str(i[1]))))
    c.sort()
    s.append("".join(i for i in c))
for iii in s:
    print(iii)
