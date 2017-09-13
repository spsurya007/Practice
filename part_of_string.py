x=str(input().strip())
y=str(input().strip())
for i in range(len(x)):
    if x[i:] in y:
        print(x[i:])
        break