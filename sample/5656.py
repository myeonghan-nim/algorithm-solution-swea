def npr(n, k):
    global w, idx, permute, permutes

    if n == k:
        permutes[idx] = permute[:]
        idx += 1
    else:
        for i in range(w):
            permute[n] = i
            npr(n + 1, k)


def shoot(c):
    global d, w, h, mat

    arr = []
    for i in range(h):
        if mat[i][c] > 0:
            arr.append((i, c, mat[i][c]))
            mat[i][c] = 0
            break

    while arr:
        i, j, l = arr.pop()
        for di, dj in d:
            for k in range(1, l):
                ni, nj = i + di * k, j + dj * k
                if 0 <= ni < h and 0 <= nj < w and mat[ni][nj]:
                    arr.append((ni, nj, mat[ni][nj]))
                    mat[ni][nj] = 0

    for j in range(w):
        for i in range(h):
            if mat[i][j]:
                c, e = i, False
                for r in range(c, h):
                    if not mat[r][j]:
                        e = r
                        break
                if e:
                    for r in range(e, -1, -1):
                        if r:
                            cnt = mat[r][j]
                            mat[r][j] = mat[r - 1][j]
                            mat[r - 1][j] = cnt
                        else:
                            mat[r][j] = 0


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    n, w, h = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(h)]

    idx, permute, permutes = 0, [0] * n, [[]] * (w ** n)
    npr(0, n)

    res = w * h + 1
    for i in range(w ** n):
        mat = [[]] * h
        for r in range(h):
            mat[r] = block[r][:]

        for j in range(n):
            shoot(permutes[i][j])

        cnt = 0
        for r in range(h):
            for c in range(w):
                if mat[r][c]:
                    cnt += 1

        res = min(res, cnt)
        if not res:
            break

    print(f'#{t + 1} {res}')
