q=[]
def sw(a):
    x=a
    n=len(x)
    if n%2==0:
        for i in range(0,n,2):
            x[i],x[i+1]=x[i+1],x[i]
    if n%2==1:
        for i in range(0,n-1,2):
            x[i],x[i+1]=x[i+1],x[i]
        x[-1],x[-2]=x[-2],x[-1]
    q.append(x)

N=int(input())
for i in range(N):
    f=list(range(1,int(input())+1))
    sw(f)
for ii in q:
    print(" ".join(str(k) for k in ii))