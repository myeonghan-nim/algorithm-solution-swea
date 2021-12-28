for t in range(int(input())):
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]

    bag = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            v, c = item[i - 1]
            res = c + bag[i - 1][j - v] if j >= v else 0
            bag[i][j] = max(bag[i - 1][j], res)

    print(f'#{t + 1} {bag[n][k]}')
