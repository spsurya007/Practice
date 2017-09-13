a=input().strip()
l=int(input())
s=[]
k,n=0,l
for i in range(len(a)//n):
    s.append(a[k:n])
    k+=l
    n+=l
ss=[]
ss.append(s[0])
ss.append(s[1][::-1])
for i in range(2,len(s)):
    if i % 2 == 0:
        ss.append(s[i])
    else:
        ss.append(s[i][::-1])
m=[]
for i in range(l):
    for j in range(len(ss)):
        m.append(ss[j][i])
print("".join(x for x in m))
