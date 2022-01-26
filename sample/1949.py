def find(r, c, digged, k, l):
    global d, n, mat, res

    for di, dj in d:
        ni, nj = r + di, c + dj
        if 0 <= ni < n and 0 <= nj < n:
            if visited[ni][nj] != 1:
                if mat[ni][nj] < mat[r][c]:
                    visited[ni][nj] = 1
                    find(ni, nj, digged, k, l + 1)
                    visited[ni][nj] = 0
                elif mat[ni][nj] >= mat[r][c] and digged:
                    if mat[ni][nj] - k < mat[r][c]:
                        t = mat[ni][nj]
                        mat[ni][nj], visited[ni][nj] = mat[r][c] - 1, 1
                        find(ni, nj, digged - 1, k, l + 1)
                        visited[ni][nj], mat[ni][nj] = 0, t

    res = max(res, l)


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for t in range(int(input())):
    n, k = map(int, input().split())

    h, mat = 0, [[]] * n
    for i in range(n):
        mat[i] = list(map(int, input().split()))
        h = max(h, max(mat[i]))

    res, visited = 0, [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == h:
                visited[i][j] = 1
                find(i, j, 1, k, 1)
                visited[i][j] = 0

    print(f'#{t + 1} {res}')
