a=list(input())
q=[]
for i in range(len(a)):
    if a[i].isdigit():
        q.append(i)

s = []
for i in range(len(a)):
    if i + 3 < len(q):
        if q[i] + 1 == q[i + 1] and q[i + 1] + 1 == q[i + 2] and q[i + 2] + 1 != q[i + 3]  :
            if i-1!=0:
                if q[i-1]==q[i]-1:
                    continue
                else:
                    s.append(''.join(str(x) for x in [a[q[i]], a[q[i + 1]], a[q[i + 2]]]))
sum=0
print(s)
for i in s:
    sum+=int(i)
print(sum)