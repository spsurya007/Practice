a,b=map(int,input().split(" "))
stock=list(map(int,input().split(" ")))
stock1=[]
for i in stock:
    stock1.append(i/b)
m=min(stock1)
stock1.remove(m)
count=0
for i in stock1:
    count+=(i-m)
if (count%2==0) or (count%2==1):
    print(int(count))
else:
    print("-1")