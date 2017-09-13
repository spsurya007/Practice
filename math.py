import math
class bear:
    a={1,2,4,4}
    dir="NESW"
    def td(self,a,dir):
        ret=0
        x,y=0,0
        m=len(a)
        for i in range(m):
            if dir[i]=='E':
                x+=a[i]
            if dir[i]=='w':
                x-=a[i]
            if dir[i]=='N':
                y+=a[i]
            if dir[i]=='S':
                y-=a[i]
            ret=sum(a)+sqrt(x*x+y*y)
            return ret
ob=bear()
