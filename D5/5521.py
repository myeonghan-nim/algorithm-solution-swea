def find(i):
    global n, mat, res, invi

    for j in range(2, n + 1):
        if mat[i][j] and j not in invi:
            res += 1
            invi.append(j)


for t in range(int(input())):
    n, m = map(int, input().split())

    mat = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a][b], mat[b][a] = 1, 1

    res, invi = 0, []
    for j in range(1, n + 1):
        if mat[1][j]:
            res += 1
            invi.append(j)

    for i in range(len(invi)):
        find(invi[i])

    print(f'#{t + 1} {res}')
