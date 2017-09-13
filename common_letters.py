a=list(input())
b=list(input())
cnt=0
for i in a:
    if i in b:
        cnt+=1
        b.remove(i)
print(cnt)