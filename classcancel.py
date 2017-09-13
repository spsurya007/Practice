min,tot=map(int,input().split(" "))
sh,sm=(input().split(":"))
a=list(input().split(" "))
arr=[]
for i in range(len(a)):
    arr.append(a[i].split(":"))
cnt=0
for i in range(min):
    if arr[i][0]<sh:
        cnt+=1
    elif arr[i][0]>=sh:
        if arr[i][1]<=sm:
            cnt+=1
if cnt>=tot:
    print("No")
else:print("Yes")