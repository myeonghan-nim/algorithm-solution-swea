for t in range(int(input())):
    v, e = map(int, input().split())

    node = [[0] * (v + 1) for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        node[a][b], node[b][a] = 1, 1

    s, g = map(int, input().split())

    q = []
    for j in range(1, v + 1):
        if node[s][j] == 1:
            q.append([s, j])

    res = 0
    while q:
        n, m = q.pop(0)
        if m == g:
            res = node[n][m]
            break
        for j in range(1, v + 1):
            if node[m][j] == 1:
                node[m][j] = node[n][m] + 1
                q.append([m, j])

    print(f'#{t + 1} {res}')
