import operator
str1=str(input())
count=0
str2=[]
res={}
for i in range(len(str1)):
    if str1[i] not in str2:
        for j in range(len(str1)):
            if str1[i] == str1[j] :
                count+=1
        res.setdefault(count,[]).append(str1[i])
        str2.append(str1[i])
        count=0
s = list(reversed(sorted(res.keys())))
for i in s:
    op=sorted(res[i])
    for j in op:
        print(j,end="")
        for l,m in res.items():
            if j in m:
                print(l)