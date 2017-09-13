
k=2
dancecost={1,5,3,4}
def mincost(k,dancecost):
    print(sum(sorted(dancecost)[:k]))
mincost(k,dancecost)