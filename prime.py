a=int(input())

if a==2:
    print("0")
elif ((2**(a-1))-1)%a==0:
    print("0")
else:
    x,y=0,0
    for i in range(a-1,1,-1):
        if ((2**(i-1))-1)%i==0:
            x=i
            break
    for j in range(a+1,100000000):
        if ((2**(j-1))-1)%j==0:
            y=j
            break
    print(y-x)