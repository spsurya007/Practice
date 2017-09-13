import sys
sys.setrecursionlimit(10000)
(x1,y1)=map(int,input().split(" "))
(x2,y2)=map(int,input().split(" "))
count=0
def path(x1,y1,x2,y2,count):
    if (x1==x2) and (y1==y2):return count
    else:
        if (x1 + 2) <= 8 and (y1 + 1) <= 8 :
            path(x1+2, y1+1,x2,y2,count+1)
        if (x1 - 2) <= 8 and (y1 + 1) <= 8:
            path(x1-2, y1+1,x2,y2,count+1)
        if (x1 + 2) <= 8 and (y1 - 1) <= 8:
            path(x1+2, y1-1,x2,y2,count+1)
        if (x1 - 2) <= 8 and (y1 - 1) <= 8:
            path(x1-2, y1-1,x2,y2,count+1)
        if (x1 + 1) <= 8 and (y1 + 2) <= 8:
            path(x1+1, y1+2,x2,y2,count+1)
        if (x1 + 1) <= 8 and (y1 - 2) <= 8:
            path(x1+1, y1-2,x2,y2,count+1)
        if (x1 - 1) <= 8 and (y1 + 2) <= 8:
            path(x1-1, y1+2,x2,y2,count+1)
        if (x1 - 1) <= 8 and (y1 - 2) <= 8:
            path(x1-1, y1-2,x2,y2,count)
        return count
path(x1,y1,x2,y2,count)
print(count)