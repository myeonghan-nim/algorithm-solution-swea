for t in range(int(input())):
    mat = [[0] * 10 for i in range(10)]

    for _ in range(int(input())):
        i, j, x, y, c = map(int, input().split())
        for m in range(i - 1, x):
            for n in range(j - 1, y):
                if mat[m][n] != c:
                    mat[m][n] += c

    res = 0
    for i in range(10):
        res += mat[i].count(3)

    print(f'#{t + 1} {res}')
