no=int(input())
names=[]
for x in range(no):
    a,b=map(str,input().strip().split(","))
    names.append((a,b))
fnd=str(input().strip())
name=dict(names)
key=list(name.keys())
print(key)
value=list(name.values())
print(value)
l1=[]
for i in range((no)):
    if value[i]==fnd:
        l1.append(i)
    else:continue
print(l1)
l2=[]
for i in l1:
    l2.append(key[i])
print(l2)
cnt=0
if len(l2)>0:
    for i in value:
        if i in l2:
            cnt+=1
        else:continue
    print(cnt)
else:print(cnt)