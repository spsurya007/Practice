def main():
    n = int(input())
    if n == 0:
        print()
        return

    s = "a"
    for i in range(1, n):
        s = chr(97 + i) + '-' + s + '-' + chr(97 + i)

    na = len(s)
    l = [s]
    for i in range(n - 1):
        k = '-' + chr(97 + i) + '-' + chr(97 + i + 1)
        s = s.replace(k, "")
        l.append(s)

    for k in reversed(l):
        a = (na - len(k)) // 2
        print("-" * a + k + "-" * a)

    for k in l[1:]:
        a = (na - len(k)) // 2
        print("-" * a + k + "-" * a)


if __name__ == '__main__':
    main()