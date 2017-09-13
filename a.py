from sys import *

def solve(_, items,p):
    for i in xrange(len(items)):
        for j in xrange(i+1,len(items)):
            if items[i] + items[j] == c:
                print "Case #%d: %d %d" %(_+1,i+1,j+1)

cases = int(raw_input())
for _ in xrange(cases):
    c = int(raw_input())
    i = int(raw_input())
    items = map(int,stdin.readline().split())
    solve(_,items,c)
