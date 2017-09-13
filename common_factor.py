n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
count=0
for i in range(2,min(a)+1):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
        if cnt==n:
            count+=1
print(count)
