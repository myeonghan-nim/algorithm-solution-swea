def find(i, j):
    global d, maze, visited, check

    visited[i][j] = 1
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < 16 and 0 <= nj < 16:
            if maze[ni][nj] == '3':
                check = 1
            elif maze[ni][nj] == '0' and not visited[ni][nj]:
                find(ni, nj)
        if check:
            break


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(10):
    n, maze = int(input()), [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        if si and sj:
            break

    check = 0
    find(si, sj)

    print(f'#{n} {check}')
