import sys
sys.setrecursionlimit(10000)
 testcases=int(input())
b=[]
for i in range(testcases):
    (x,y)=map(int,input().split(" "))
    f=[]
    for m in range(x):
        f.append(list(map(int,input().split(" "))))
    b.append(f)
def eq(a,count=0):
    def w_r(i, j):
        if a[i][j] == maxi:
            if j + 1 < len(a[0]):
                a[i] [j + 1] = maxi
            if i + 1 < len(a):
                a[i + 1] [j] = maxi
            if i + 1 < len(a) and j + 1 < len(a[0]):
                a[i + 1] [j + 1] = maxi
            if i - 1 < len(a) and i - 1 >= 0 and j - 1 < len(a[0]) and j - i >= 0:
                a[i - 1] [j - 1] = maxi
            if i - 1 < len(a) and i - 1 >= 0:
                a[i - 1][j] = maxi
            if j - 1 >= 0 and j - 1 < len(a[0]):
                a[i][ j - 1] = maxi
            if i + 1 < len(a) and j - 1 < len(a[0]) and j - 1 >= 0:
                a[i + 1][ j - 1] = maxi
            if i - 1 < len(a) and i - 1 >= 0 and j + 1 < len(a[0]):
                a[i - 1][ j + 1] = maxi
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==a[0][0]:
                continue
            else:
                maxi = 0
                for i in range(len(a)):
                    if maxi < max(a[i]):
                        maxi = max(a[i])
                q=[]
                for i in range(len(a)):
                    for j in range(len(a[i])):
                        if a[i][j]==maxi:
                            q.append([i,j])
                for _ in range(len(q)):
                    w_r(a[_][0],a[_][1])
                    count+=1
                    eq(a)
    return count
for i in range(testcases):
    x=eq(b[i],0)
    print(x)