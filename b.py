from sys import *

def solve(_, words):
    print "Case #%d:" %(_+1),
    for w in words[::-1]:
        print w,
    print

cases = int(raw_input())
for _ in xrange(cases):
    words = map(str,stdin.readline().split())
    solve(_,words)
