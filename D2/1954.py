for t in range(int(input())):
    n = int(input())
    mat = [[0] * n for _ in range(n)]

    go, num, i, j = 1, 0, 0, -1
    while n > 0:
        for k in range(n):
            num += 1
            j += go
            mat[i][j] = num
        n = n - 1
        for k in range(n):
            num += 1
            i += go
            mat[i][j] = num
        go *= -1

    print(f'#{t + 1}')
    for r in range(len(mat)):
        print(' '.join(map(str, mat[r])))
