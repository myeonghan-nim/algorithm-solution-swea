di, dj = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

for t in range(int(input())):
    n, m = map(int, input().split())

    board = [[0] * n for _ in range(n)]
    board[n // 2][n // 2 - 1], board[n // 2 - 1][n // 2] = 1, 1
    board[n // 2 - 1][n // 2 - 1], board[n // 2][n // 2] = 2, 2

    for _ in range(m):
        ti, tj, c = map(int, input().split())

        i, j = ti - 1, tj - 1
        board[i][j] = c

        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if board[ni][nj] != c and board[ni][nj]:
                    points = []
                    while True:
                        if not (0 <= ni < n and 0 <= nj < n) or not board[ni][nj]:
                            break
                        elif board[ni][nj] != c:
                            points.append([ni, nj])
                        elif board[ni][nj] == c:
                            for p in points:
                                board[p[0]][p[1]] = c
                            break
                        ni += di[k]
                        nj += dj[k]

    b, w = 0, 0
    for _ in range(n):
        b += board[_].count(1)
        w += board[_].count(2)

    print(f'#{t + 1} {b} {w}')
