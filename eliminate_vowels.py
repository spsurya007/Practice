a=input()
vp=[]
for i in range(len(a)):
    if a[i] in ['a','e','i','o','u']:
        vp.append(i)
s=a[::-1]
res=""
for i in range(len(a)):
    if i in vp:
        continue
    else:
        res+=s[i]
print(res)