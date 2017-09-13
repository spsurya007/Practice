n=int(input())
a=list(map(str,input().split(" ")))
count=0
for i in range(len(a)-2):
    if ((int(a[i]) > int(a[i + 1]) > int(a[i + 2])) or (int(a[i]) < int(a[i + 1]) < int(a[i + 2]))):
        count += 1
    else:
        continue
print(count)