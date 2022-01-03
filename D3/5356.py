for t in range(int(input())):
    mat = [list(input()) for i in range(5)]

    n = 0
    for i in range(5):
        n = max(n, len(mat[i]))

    for i in range(5):
        if len(mat[i]) != n:
            mat[i] += [''] * (n - len(mat[i]))

    print(f'#{t + 1}', end=' ')
    for i in range(n):
        for j in range(5):
            print(mat[j][i], end='')
    print()
