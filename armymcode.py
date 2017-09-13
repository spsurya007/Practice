n=int(input())
k=int(input())
a=str(input())
a=list(a)
b=str(input())
c= []
for i in range(len(b)):
    if i + n <= len(b):
        c.append(list(b[i:i + n]))
count=0
for i in range(len(c)):
    cnt=0
    for j in c[i]:
        if j in a:
            cnt+=1
            if cnt==n:
                count+=1
                cnt=0
print(count)