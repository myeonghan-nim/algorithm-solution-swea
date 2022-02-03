def find(i, j, n):
    global d, maze

    arr, maze[i][j] = [[i, j]], '1'

    while arr:
        p, q = arr.pop()
        for di, dj in d:
            ni, nj = p + di, q + dj
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '3':
                    return 1
                if maze[ni][nj] == '0':
                    arr.append([ni, nj])
                    maze[p][q] = '1'

    return 0


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    n = int(input())
    maze = [list(input()) for _ in range(n)]

    can_start, si, sj = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                can_start, si, sj = 1, i, j
            if can_start:
                break
        if can_start:
            print(f'#{t + 1} {find(si, sj, n)}')
            break
