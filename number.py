n=str(input())
num=['0','1','2','3','4','5','6','7','8','9']
num1=[]
while num!=num1:
    for i in range(len(n)):
        if n[i] not in num1:
            num1.append(n[i])
        else:continue
