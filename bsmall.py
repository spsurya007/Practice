n=int(input())
new=[]
for i in range(n):
    string=list(map(str,input().split(" ")))
    m=string[::-1]
    new.append(m)
for i in range(len(new)):
    print("Case #"+str(i+1)+": "+" ".join([str(x) for x in new[i]])+" ")