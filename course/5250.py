def find():
    global d, n, mat, check

    q = [(0, 0)]
    while q:
        i, j = q.pop(0)
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                t, diff = check[i][j] + 1, mat[ni][nj] - mat[i][j]
                if diff >= 1:
                    t += diff
                if check[ni][nj] > t:
                    check[ni][nj] = t
                    q.append((ni, nj))


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    check = [[10001 * 100] * n for _ in range(n)]
    check[0][0] = 0
    find()

    print(f'#{t + 1} {check[n - 1][n - 1]}')
