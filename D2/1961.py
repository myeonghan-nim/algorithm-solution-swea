for t in range(int(input())):
    n = int(input())
    mat = [list(input().split()) for _ in range(n)]

    rev = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rev[i][j] = mat[j][i]

    print(f'#{t + 1}')
    for r in range(n):
        print(
            ''.join(rev[r][::-1]),
            ''.join(mat[::-1][r][::-1]),
            ''.join(rev[::-1][r])
        )
