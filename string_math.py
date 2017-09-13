a=input().strip()
x,y=0,0
for i in range(len(a)):
    if a[i].isalpha():
        x=i
        y=a[i]
print(y)
if y == 'a' or y =='A':
    print(int(a[0:x])+int(a[x+1:]))
elif y == 's' or y =='S':
    print(int(a[0:x])-int(a[x+1:]))
elif y == 'm' or y == 'M':
    print(int(a[0:x])*int(a[x+1:]))
elif y == 'd'or y == 'D':
    print(int(a[0:x])//int(a[x+1:]))
