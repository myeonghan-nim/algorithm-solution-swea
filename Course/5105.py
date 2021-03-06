def find(i, j, r):
    global d, n, maze, res

    if maze[i][j] == '3':
        res = min(res, r - 1)
    else:
        maze[i][j] = '1'
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] != '1':
                    find(ni, nj, r + 1)
        maze[i][j] = '0'


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    n = int(input())
    maze = [list(input()) for _ in range(n)]

    si, sj = 0, 0
    can_start, res = 0, n ** 2 + 1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                can_start, si, sj = 1, i, j
            if can_start:
                break
        if can_start:
            find(si, sj, 0)

    if res == n ** 2 + 1:
        res = 0

    print(f'#{t + 1} {res}')
