n,m=map(int,input().split(" "))
x=1
for i in range(1,min(n,m)+1):
    x*=i
print(x)


"""
from fractions import gcd
from functools import reduce
n=int(input())
a=list(map(int,input().split()))
print(reduce(gcd,a))
"""