a=str(input().strip())
mid=len(a)//2
m,k=[],mid+1
for i in range(mid):
    m.append(" "*(i)+a[i]+" "*(len(a)-k)+a[-(i+1)]+" "*(i))
    k+=1
for x in m:
    print(x)
print(" "*(mid//2)+a[mid]+" "*(mid//2))
for x in m[::-1]:
    print(x)