def find(s, g):
    global v, mat

    arr = []
    for j in range(v + 1):
        if mat[s][j] == 1:
            arr.append([s, j])

    while arr:
        q = arr.pop()[1]
        if q == g:
            return 1

        for j in range(v + 1):
            if mat[q][j] == 1:
                arr.append([q, j])

    return 0


for t in range(int(input())):
    v, e = map(int, input().split())

    mat = [[0] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        i, j = map(int, input().split())
        mat[i][j] = 1

    print(f'#{t + 1} {find(*list(map(int, input().split())))}')
