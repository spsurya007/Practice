N = int(input())
op = []
for i in range(N):
    n, q = map(int, input().split())
    for j in range(q):
        a, b, c = map(int, input().split())
        if abs(b - a) == c:
            y = "yes"
            continue
        else:
            y = "no"
            break
    op.append(y)
for i in op:
    print(i)
