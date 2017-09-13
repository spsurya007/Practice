a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
d=list(map(int,input().split(" ")))

if b[0]==d[0]:
    if a[0]==b[0]:
        if a[1] in range(min(b[1],d[1]),max(b[1],d[1])+1):
            print("Yes")
        else:
            print("no")
    elif c[0]==b[0]:
        if c[1] in range(min(b[1],d[1]),max(b[1],d[1])+1):
            print("Yes")
        else:
            print("no")
elif b[1]==d[1]:
    if a[1]==b[1]:
        if a[0] in range(min(b[0], d[0]), max(b[0], d[0]) + 1):
            print("yes")
        else:
            print("no")
    elif c[1]==b[1]:
        if c[0] in range(min(b[0], d[0]), max(b[0], d[0]) + 1):
            print("yes")
        else:
            print("no")
if a[0]==c[0]:
    if b[0]==a[0]:
        if b[1] in range(min(c[1], a[1]), max(c[1], a[1]) + 1):
            print("Yes")
        else:
            print("no")
    elif d[0]==a[0]:
        if d[1] in range(min(c[1], a[1]), max(c[1], a[1]) + 1):
            print("Yes")
        else:
            print("no")
elif a[1]==c[1]:
    if b[1]==c[1]:
        if b[0] in range(min(c[0], a[0]), max(c[0], a[0]) + 1):
            print("yes")
        else:
            print("no")
    elif d[1]==c[1]:
        if d[0] in range(min(c[0], a[0]), max(c[0], a[0]) + 1):
            print("yes")
        else:
            print("no")