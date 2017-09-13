a,b=map(int,input().split(" "))
if b<=a:
    mat=[[0] * a for i in range(a)]
    for i in range(b):
        mat[i][i]=1
    s=[[str(x) for x in y] for y in mat ]
    lens=[max(map(len,col)) for col in zip(*s)]
    fmt=" ".join("{{:{}}}".format(x) for x in lens)
    table=[fmt.format(*y) for y in s]
    print("\n".join(table))
else:
    print("-1")
