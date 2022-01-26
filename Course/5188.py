def find(i, j, cnt):
    global d, n, mat, res

    if cnt > res:
        return

    for di, dj in d:
        ni, nj = i + di, j + dj
        if ni == n - 1 and nj == n - 1:
            res = min(res, cnt + mat[ni][nj])
        elif ni < n and nj < n:
            find(ni, nj, cnt + mat[ni][nj])


d = [(0, 1), (1, 0)]
for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res = 10 * (2 * n - 1)
    find(0, 0, mat[0][0])

    print(f'#{t + 1} {res}')
