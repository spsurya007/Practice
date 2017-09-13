x=int(input())
s=[]
for i in range(x):
    n=int(input())
    s.append(list(map(int,input().split(" "))))
def temple(a,k=0):
    ans=0
    mid=len(a)//2
    if a[0:mid]==a[len(a):mid:-1]:
        if a[mid-1]+1==a[mid]:
            ans=0+k
        else :
            ans=(a[mid]-(a[mid-1]+1))+k
    else:
        cnt=0
        for i,j in zip(a[0:mid],a[len(a):mid:-1]):
            if i==j:
                continue
            else:
                cnt+=(abs(i-j))
        ans=cnt+k

    m.append(ans)
for i in range(len(s)):
    m=[]
    if len(s[i])%2!=0 and len(s[i])>2:
        temple(s[i],k=0)
        print(m[0])
    elif len(s[i])==2:
        print(min(s[i]))
    else:
        temple(s[i][0:len(s[i])-1],s[i][len(s[i])-1])
        temple(s[i][1:len(s[i])],s[i][0])
        print(min(m))