def produce(n, k, c):
    global mat, res, used

    if c > res:
        return

    if n == k:
        if res > c:
            res = c
    else:
        for i in range(k):
            if not used[i]:
                used[i] = 1
                produce(n + 1, k, c + mat[n][i])
                used[i] = 0


for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res, used = 100 * n, [0] * n
    produce(0, n, 0)

    print(f'#{t + 1} {res}')
