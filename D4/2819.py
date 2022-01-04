def make(i, j, num):
    global mat, res, d

    num += str(mat[i][j])
    if len(num) == 7:
        res.add(num)
    else:
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4:
                make(ni, nj, num)


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(int(input())):
    mat = [list(map(int, input().split())) for _ in range(4)]

    res = set()
    for i in range(4):
        for j in range(4):
            make(i, j, '')

    print(f'#{t + 1} {len(res)}')
