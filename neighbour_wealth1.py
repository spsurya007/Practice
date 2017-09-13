x,y=map(int,input().split(" "))
a=[]
for i in range(x):
    a.append(list(map(int,input().split(" "))))
maxi=0
for i in range(x):
    if max(a[i])>maxi:
        maxi=max(a[i])
print(maxi)
count=0
for i in range(x):
    for j in range(y):
        if a[i][j]==maxi:
            continue
        else:
            if j + 1 < len(a[0]):
                if a[i] [j + 1] == maxi:
                    a[i][j]=maxi
            if i + 1 < len(a):
                if a[i + 1] [j] == maxi:
                    a[i][j]=maxi
            if i + 1 < len(a) and j + 1 < len(a[0]):
                if a[i + 1] [j + 1] == maxi:
                    a[i][j]=maxi
            if i - 1 < len(a) and i - 1 >= 0 and j - 1 < len(a[0]) and j - i >= 0:
                if a[i - 1] [j - 1] == maxi:
                    a[i][j]=maxi
            if i - 1 < len(a) and i - 1 >= 0:
                if a[i - 1][j] == maxi:
                    a[i][j] = maxi
            if j - 1 >= 0 and j - 1 < len(a[0]):
                if a[i][ j - 1] == maxi:
                    a[i][j] = maxi
            if i + 1 < len(a) and j - 1 < len(a[0]) and j - 1 >= 0:
                if a[i + 1][ j - 1] == maxi:
                    a[i][j] = maxi
            if i - 1 < len(a) and i - 1 >= 0 and j + 1 < len(a[0]):
                if a[i - 1][ j + 1] == maxi:
                    a[i][j] = maxi
            count+=1
print(a)
print(count)