a=list(map(int,input().split(" ")))
b=[]
for i in range(len(a)):
    cnt=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            cnt+=1
    if cnt==0:
        b.append(a[i])
print(" ".join(str(x) for x in b))