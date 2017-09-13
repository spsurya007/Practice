n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(list(map(int,input().split(" "))))
for i in a:
    print(i.count(max(i)))