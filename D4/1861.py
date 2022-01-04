def find(i, j, length, num):
    global d, n, rooms, route, res, visited

    if res <= length:
        res = length

    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if rooms[ni][nj] - rooms[i][j] == 1:
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    find(ni, nj, length + 1, num)
                    visited[ni][nj] = 0

    if length == res:
        route.append((num, length))


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]

    route, res = [], 1
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            find(i, j, 1, rooms[i][j])

    route = sorted(route, key=lambda x: (-x[1], x[0]))
    print(f'#{t + 1} {route[0][0]} {res}')
