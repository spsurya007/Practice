n, m = map(int, input().split())
glflag = False
for i in range(m):
    arr = list(map(int, input().split()))
    used = [0] * n
    flag = False
    for j in range(1, len(arr)):
        if arr[j] * used[abs(arr[j]) - 1] < 0:
            flag = True
            break
        else:
            if arr[j] < 0:
                used[abs(arr[j]) - 1] = -1
            else:
                used[abs(arr[j]) - 1] = 1

    if not flag:
        print('YES')
        glflag = True
        break
if not glflag:
    print('NO')