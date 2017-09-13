import math
N=int(input())
q=[]
for i in range(N):
    k=int(input())
    l=long(k)
    l=list(map(int,input().split()))
    s = 1e9
    index = -9999
    for i in range(k):
        c = sum(l[0:i+1]) + sum(l[i:])
        if c < s:
            s = c
            index = i
    print(index+1)