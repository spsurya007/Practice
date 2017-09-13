a=list(input())
x=int(input())
y=int(input())
c=[]
for i in a:
    if ord(str(i)) in range(97,123):
        c.append(chr(ord(i)+x) if ord(i)+x < 123 else chr((96+x)))
    elif ord(str(i)) in range(48,58):
        c.append(str(int(i)+y))
    else:
        c.append(i)
print("".join(str(l) for l in c))