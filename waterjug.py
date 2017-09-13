x=int(input())
y=int(input())
z=int(input())
count=1
if x==z or y==z:
    print(count)
elif x<z and y<z:
    print("-1")
else:
    maxi=max(x,y)
    mini=min(x,y)
    if z==maxi-mini:
        count+=1
        print(count)