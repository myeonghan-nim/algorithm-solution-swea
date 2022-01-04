for t in range(int(input())):
    n, m = int(input()), int(input())

    diff = [[501] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        diff[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i != k:
                for j in range(1, n + 1):
                    if j != i and j != k:
                        diff[i][j] = min(diff[i][k] + diff[k][j], diff[i][j])

    cnt = 0
    for i in range(1, n + 1):
        r = 0
        for j in range(1, n + 1):
            if i != j:
                if diff[i][j] != 501:
                    r += 1
                if diff[j][i] != 501:
                    r += 1
        if r == n - 1:
            cnt += 1

    print(f'#{t + 1} {cnt}')
