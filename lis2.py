def lis(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)
                  + [d[i]])
    return max(l, key=len)
a=lis(['a','b','c','b','c','b','c','d'])
print(a)