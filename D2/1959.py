for t in range(int(input())):
    n, m = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))

    res = 0
    for i in range(abs(n - m) + 1):
        temp = 0
        if n <= m:
            for j in range(n):
                temp += a[j] * b[j + i]
        else:
            for j in range(m):
                temp += a[j + i] * b[j]
        if res < temp:
            res = temp

    print(f'#{t + 1} {res}')
