def npr(n, k, t, r):
    global arr, used, permute, q, res

    if r > res:
        return

    if n == k:
        r += abs(permute[-1][0] - permute[-2][0])
        r += abs(permute[-1][1] - permute[-2][1])
        if res > r:
            res = r
    else:
        for i in range(t):
            if used[i] == 0:
                used[i], permute[n] = 1, q[i]
                c = abs(permute[n][0] - permute[n - 1][0])
                c += abs(permute[n][1] - permute[n - 1][1])
                npr(n + 1, k, t, r + c)
                used[i] = 0


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))

    co, h, q = tuple(arr[:2]), tuple(arr[2:4]), []
    for i in range(4, 2 * (n + 2), 2):
        q.append((arr[i], arr[i + 1]))

    res, used, permute = 100 ** 10, [0] * n, [co] + [0] * n + [h]
    npr(1, n + 1, n, 0)

    print(f'#{t + 1} {res}')
