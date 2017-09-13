x=int(input())
y=int(input())
xmat,ymat=[],[]
for i in range(x):
    xmat.append(list(map(int,input().strip().split(" "))))
for i in range(y):
    ymat.append(list(map(int,input().strip().split(" "))))
print(xmat)
print(ymat)
t=[]
for i in range((x-y)+1):
    for j in range((x-y)+1):
        temp=[[0]*2]*2
        for k in range(i,i+y):
            a=0
            a+=1
            for l in range(j,j+y):
                b=0
                b+=1
                temp[a][b]=xmat[k][l]
    t.append(list(temp))
print(temp)