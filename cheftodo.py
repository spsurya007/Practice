n=int(input())
a=[]
for i in range(n):
    a.append(list(map(str,input())))
def check(a):
    count=0
    for i in range(len(a)):
        if i+1<len(a):
            if ord(a[i])<=ord(a[i+1]):
                count+=1
    if count==len(a)-1:print("yes")
    else:print("no")
for i in a:
    check(i)