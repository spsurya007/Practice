a=input().strip()
q=[]
k=0
for i in range(len(a)):
    if a[i].isalpha():
        q.append(a[k:i+1])
        k=i+1
s=[]
for i in q:
    s.append(i[-1]*int(i[:-1]))
print("".join(str(x) for x in s))