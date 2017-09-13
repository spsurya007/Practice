s=input()
op,cl,r=[],[],[]
for i in range(0,len(s)):
    if s[i]=="(":
        op.append(i)
    elif s[i]==")":
        cl.append(i)
cl1,r1=[],[]
for i in range(len(cl)):
    if len(op)>0:
        if op[0]>cl[i]:
            r1.append(cl[i])
    else:
        r1.append(cl[i])
r1=list(set(r1))
r1.sort()
if len(op)>=len(cl):
    if len(cl)>0:
        op1=[]
        for i in range(len(cl)):
            if op[i]<cl[i]:
                op1.append(op[i])
            else:
                r1.append(op[i])
        r=list(set(op)-set(op1))
    else:
        for i in range(len(op)):
            r1.append(op[i])
    rem=(r1+r)
elif len(cl)>len(op):
    cl2=[]
    for i in range(len(op)):
        cl2.append(cl[i])
    r=list(set(cl)-set(cl2))
    rem=(r1+r)
rem=list(set(rem))
rem.sort()
modrem=[]
for i in range(0,len(rem)):
    modrem.append(rem[i]-i)
modrem.sort()
for i in range(0,len(modrem)):
    s=s[0:modrem[i]]+s[modrem[i]+1:]
print(s)
