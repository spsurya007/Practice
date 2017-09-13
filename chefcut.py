import itertools
t=int(input())
qs=[]
for i in range(t):
    (len,val,mod)=map(int,input().split(" "))
    qs.append((len,val,mod))
for i in range(t):
    min=(qs[i][0]//qs[i][1])+(qs[i][0]%qs[i][1])
    if qs[i][0]%qs[i][1] == 0:
        print((min),end=' ')
        print("1")
    else:
        if min-1>1:
            cnt=0
            for x in range(1,min+1):
                for y in range(1,qs[i][0]):
                    if (y-x)<=3 and (y-x)!=0 and (qs[i][0]-y)<=3:
                        cnt+=1
            print(min,end=' ')
            print(cnt%qs[i][2])
        else:
            if min-1==1:
                print(min,end=' ')
                print(qs[i][1])
            elif min-1<0:
                print("1",end=' ')
                print("0")
