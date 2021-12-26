for t in range(10):
    n = int(input())
    mat = [list(input()) for i in range(8)]

    rev = [['' for i in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            rev[i][j] = mat[j][i]

    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            r, c = mat[i][j:j + n], rev[i][j:j + n]
            cnt += (r == r[::-1]) + (c == c[::-1])

    print(f'#{t + 1} {cnt}')
