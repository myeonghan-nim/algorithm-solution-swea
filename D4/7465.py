def rep(n):
    global p

    while p[n] != n:
        n = p[n]

    return n


for t in range(int(input())):
    n, m = map(int, input().split())

    p = list(range(n + 1))
    for _ in range(m):
        n1, n2 = map(int, input().split())
        p[rep(n2)] = rep(n1)

    cnt = 0
    for i in range(1, n + 1):
        if p[i] == i:
            cnt += 1

    print(f'#{t + 1} {cnt}')
