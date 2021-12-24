for t in range(int(input())):
    n, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    rev = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rev[i][j] = mat[j][i]

    cnt = 0
    for data in (mat, rev):
        for i in range(n):
            if data[i].count(1) >= k:
                for idx in range(n - k + 1):
                    if data[i][idx:idx + k].count(1) == k:
                        if data[i][idx:idx + k + 1].count(1) != k + 1:
                            if data[i][idx - 1:idx + k].count(1) != k + 1:
                                cnt += 1

    print(f'#{t + 1} {cnt}')
