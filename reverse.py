a=list(map(str,input()))
s=[]
for i in range(1,len(a)+1):
    s.append(a[-i])
m=list(zip(a,s))
p = []
for i in range(len(m)):
    if m[i][0] == m[i][1]:
        continue
    else:
        p.append((m[i][0], m[i][1]))

if len(p)>2:
    print('NO')
else:
    if len(p)==0:
        print("NO")
    elif (p[0][0]==p[1][1] and p[0][1]==p[1][0]):
        print("YES")
