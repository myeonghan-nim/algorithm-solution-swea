for T in range(int(input())):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    move, res = 0, 0
    while move + m <= n:
        for j in range(n):
            mini = 0
            for i in range(j, j + m):
                if move + m <= n and j + m <= n:
                    mini += sum(mat[i][move:move + m])
            res = max(mini, res)
        move += 1

    print(f'#{T + 1} {res}')
