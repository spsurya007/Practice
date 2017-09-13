jumps=int(input())
slides=int(input())
n=int(input())
wall=[]
for i in range(n):
    wall.append(int(input()))
count=0
for i in range(len(wall)):
    if wall[i]<=jumps:
        count+=1
    else:
        while wall[i]>0:
            if wall[i]>jumps:
                wall[i]-=jumps
                wall[i]+=slides
                count+=1
            if wall[i]<=jumps:
                wall[i]-=jumps
                count+=1
print(count)