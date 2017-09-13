testcase=int(input())
sol=[]
s1=[]
for i in range(testcase):
    credit=int(input())
    item=int(input())
    items=list(map(int,input().split(" ")))
    for i in range(item):
        for j in range(item):
            if items[i]+items[j]==credit:
                sol.append(i+1)
                sol.append(j+1)
            s=sol[0:2]
            s1.append(s)
print(s1)