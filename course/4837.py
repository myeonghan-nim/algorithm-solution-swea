def ncr(n, r):
    global k, cnt, p, arr

    if not r:
        if sum(p) == k:
            cnt += 1
    elif r > n:
        return
    else:
        p[r - 1] = arr[n - 1]
        ncr(n - 1, r - 1)
        ncr(n - 1, r)


for t in range(int(input())):
    n, k = map(int, input().split())
    cnt, p, arr = 0, [0] * n, list(range(1, 13))
    ncr(12, n)
    print(f'#{t + 1} {cnt}')
