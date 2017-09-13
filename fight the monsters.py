(n,hit,cntmax)=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
a.sort()
print(a)
def df(a,i=0,cnt=0):
    if cnt<cntmax:
        if a[i]>0:
            a[i]-=hit
            cnt+=1
            if a[i]>0:
                df (a,i,cnt)
            elif (a[i]<=0):
                i+=1
                df (a,i,cnt)
df(a)
print(a)
count=0
for i in a:
    if i<=0:
        count+=1
print(count)