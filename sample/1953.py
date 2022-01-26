def check(num):
    if num == 1:
        return [0, 1, 2, 3]
    elif num == 2:
        return [1, 3]
    elif num == 3:
        return [0, 2]
    elif num == 4:
        return [0, 3]
    elif num == 5:
        return [0, 1]
    elif num == 6:
        return [1, 2]
    else:
        return [2, 3]


def running(n, m, r, c, l):
    global d, union, mat

    s, e = -1, -1
    q, visited = [[0, 0] for _ in range(n * m)], [[0] * m for _ in range(n)]

    e += 1
    q[e], visited[r][c] = [r, c], 1
    while s != e:
        s += 1
        i, j = q[s]

        if visited[i][j] >= l:
            break

        tunnels = check(mat[i][j])
        for t in tunnels:
            u, ni, nj = union[t], i + d[t][0], j + d[t][1]
            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj]:
                    if mat[ni][nj] in u:
                        e += 1
                        q[e], visited[ni][nj] = [ni, nj], visited[i][j] + 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                cnt += 1

    return cnt


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
union = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]
for t in range(int(input())):
    n, m, r, c, l = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t + 1} {running(n, m, r, c, l)}')
