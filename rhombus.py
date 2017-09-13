n=int(input())
p=2*n
a=[["#"]*p]*p
m=list(range(0,n+1,2))
for f in m:
    k=-1
    for i in range(f,n):
        a[f][k]="/"
        a[f][i]="\\"
        k-=1
print(a)