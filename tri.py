


class TriangleMaking:
    def maxPerimeter(self, a, b, c):
        L = [a, b, c]
        L.sort()
        if L[0] + L[1] <= L[2]:
            return 2 * (L[0] + L[1]) - 1
        else:
            return sum(L)

o=TriangleMaking()
m=o.maxPerimeter(1,100,1)
print(m)