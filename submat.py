n=int(input().strip())
m=int(input().strip())
l1,l2=[],[]
for i in range(n):
    l1.append(list(map(int,input().strip().split(" "))))
for i in range(m):
    l2.append(list(map(int,input().strip().split(" "))))
(k,l)=(-1,-1)
f=0
for i in range(n):
    for j in range(n):
        if (k,l)==(-1,-1):
            if l1[i][j]==l2[0][0]:
                k,l=i,j
        else:
            if i-k>=0 and i-k<m and j-l>=0 and j-l<m:
                if l1[i][j]==l2[i-k][j-l]:
                    if (i-k,j-l)==(m-1,m-1):
                        f=1
                        break
                else:
                    (k,l)=(-1,-1)
            else:None
print(l1)
print(l2)
if f==1:
    print("TRUE")
else:print("FALSE")