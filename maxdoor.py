n,m=map(int,input().split(" "))
a=[]
for _ in range(n):
    a.append(list(map(int,input().strip().split(" "))))
f=[]
f.append(a[0][0])
def c(i=0, j=0):
    if (i + 1) < n and (j + 1) < m:
        if a[i][j + 1] > a[i + 1][j]:
            f.append(a[i][j + 1])
            c(i, j + 1)
        else:
            f.append(a[i + 1][j])
            c(i + 1, j)
    else:
        if i>j:
            if j==m-1:
                for k in range(i+1,n):
                    f.append(a[k][j])
            else:
                for k in range(j+1,m):
                    f.append(a[i][k])
        elif j>i:
            for k in range(i+1,n):
                f.append(a[k][j])
c()
print(f)
print(sum(f))
