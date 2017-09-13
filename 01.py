import sys
sys.setrecursionlimit(10000)
n=int(input())
g=[]
for i in range(n):
    g.append(int(input()))
print(g)
sm=[]
s=['0','1']
def com(s):
    if len(s)<1001:
        a=['0']*len(s)
        for i in range(len(s)):
            if s[i]=='1':
                a[i]='0'
            if s[i]=='0':
                a[i]='1'
        s=s+a
        sm.append(s)
        com(s)
com(s)
for i in g:
    print(sm[-1][i])


