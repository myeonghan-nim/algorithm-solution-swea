for t in range(int(input())):
    n, m = map(int, input().split())
    row = [list(input()) for i in range(n)]

    col = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            col[i][j] = row[j][i]

    res = ''
    for i in range(n):
        for j in range(n - m + 1):
            for mat in (row, col):
                if mat[i][j:j + m] == mat[i][j:j + m][::-1]:
                    res = ''.join(mat[i][j:j + m])
                    break
            if res:
                break
        if res:
            break

    print(f'#{t + 1} {res}')
