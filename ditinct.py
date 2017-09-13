x,y=map(int,input().split(" "))
a = [str(x) for x in input().split()]
b = [str(x) for x in input().split()]
cnt=0
for i in a:
    if i not in b:
        cnt+=1
for i in b:
    if i not in a:
        cnt+=1
print(a)
print(b)
print(cnt)