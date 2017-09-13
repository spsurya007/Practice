a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
d=int(input('enter d value'))
class rick():
    def caught(self,a,b,c,d):
        m=[]
        n=[]
        for i in range(100):
            m.append(b+i*a)
        for i in range(100):
            n.append(d+i*c)
        s=set(m)&set(n)
        if s==set():
            print("-1")
        else:
            q=list(s)[0]
            print(q)
obj=rick()
obj.caught(a,b,c,d)