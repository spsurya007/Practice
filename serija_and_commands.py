N=int(input())
op=[]

def one(i):
    for j in range(i[1] - 1, i[2]):
        a[j] += 1
def two(i):
    for k in range(i[1] - 1, i[2]):
        if com[k][0] == 1:
            one(com[k])
        elif com[k][0] == 2:
            two(com[k])

for i in range(N):
    n,m=map(int,input().split())
    a=[0]*n
    com = [list(map(int, input().split())) for x in range(m)]

    for k in range(0, m):
        if com[k][0] == 1:
            one(com[k])
        if com[k][0] == 2:
            two(com[k])

    op.append(a)

for i in op:
    print(" ".join(str(x) for x in i))
