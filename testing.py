a,b=[int(x) for x in input("enter").split()]
c,d=[int(x) for x in input("enter").split()]


class rick():
    def caught(self,a,b,c,d):
        m=[]
        n=[]
        for i,j in range(100):
            m.append(b+i*a)
            n.append(d+i*c)
        s=set(m)&set(n)
        if s==set():
            print("-1")
        else:
            q=list(s)[0]
            print(q)
obj=rick()
obj.caught(a,b,c,d)