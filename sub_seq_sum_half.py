def sub(a,n):
    sum=[]
    sum.append(0)
    for i in range(1,n+1):
        sum[i]=sum[i-1]+a[i-1]-'0'
    ans=0
    for j in range(2,n+1,2):
        for k in range(0,n-1):
            x=k+j-1
            if (sum[i+j//2]-sum[k]==sum[k+j]-sum[k+j//2]):
                ans=max(ans,j)
    print(ans)

a='123123'
sub(a,0)