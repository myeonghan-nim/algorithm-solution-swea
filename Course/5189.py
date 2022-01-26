def find(n, k):
    global used, route, routes, points

    if n == k:
        routes += [[1] + route + [1]]
    else:
        for i in range(k):
            if not used[i]:
                used[i], route[n] = 1, points[i]
                find(n + 1, k)
                used[i] = 0


for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    used, route, routes = [0] * (n - 1), [0] * (n - 1), []
    points = list(range(2, n + 1))
    find(0, n - 1)

    res = 100 * (n + 1)
    for r in routes:
        m = 0
        for i in range(n):
            m += mat[r[i] - 1][r[i + 1] - 1]
        if res >= m:
            res = m

    print(f'#{t + 1} {res}')
