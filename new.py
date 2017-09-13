class Ropestring:
    def makerope(self,s):
        le=[]
        t=0
        for i in s+'.':
            if i=='.':
                if t: le.append(t)
                t=0
            else:
                t+=1
        o0=[]
        o1=[]
        for i in le:
            if i%2: o1.append(i)
            else: o0.append(i)
        o0.sort(reverse=True)
        o1.sort(reverse=True)
        for i in o1: o0.append(i)
        out=".".join(map(lambda i:'-'*i,o0))
        while len(out)<len(s): out+='.'
        return out
ob=Ropestring()
m=ob.makerope("---.--.--.---..-")
print(m)