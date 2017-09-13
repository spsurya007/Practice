n=int(input())
a=[]
for i in range(n):
    a.append(list(map(str,input().split(" "))))
mini=(int(a[0][1]))*(int(a[0][2]))/100
k=0
for i in range(1,n):
    if ((int(a[i][1]))*(int(a[i][2]))/100) < mini :
        mini=(int(a[i][1])*int(a[i][2]))/100
        k=i
print(mini)
print(a[k][0])