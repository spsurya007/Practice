from __future__ import division,print_function
import sys
class user:
    def __init__(self,v0,v1,v2,v3,v4):
        self.a=v0
        self.b=v1
        self.c=v2
        self.d=v3
        self.e=v4
    def __repr__(self):
        return 'user(%r,%r,%r,%r,%r)'\
               %(self.a,self.b,self.c,self.d,self.e)
color=user('bluee','red','yellow','orange','green')
city=user('chennai','mumbai','goa','bangalore','tricy')
for i in [color,city]:
    print(vars(i))
print(list(map(sys.getsizeof,map(vars,[color,city]))))