for _ in range(10):
    t = int(input())
    mat = [list(map(int, input().split())) for i in range(100)]

    r = c = s = rs = 0
    for i in range(100):
        rt = ct = 0
        for j in range(100):
            rt += mat[i][j]
            ct += mat[j][i]
        s += mat[i][i]
        rs += mat[i][99 - i]
        if rt > r:
            r = rt
        if ct > c:
            c = ct

    res = max(r, c, s, rs)
    print(f'#{t} {res}')
