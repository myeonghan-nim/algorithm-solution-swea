def charge(cnt, idx, l, n):
    global arr, res

    if l + idx >= n:
        if res >= cnt:
            res = cnt
    else:
        max_l, n_idx = 0, 0
        for i in range(1, l + 1):
            t = (idx + i) + arr[idx + i]
            if max_l < t:
                max_l, n_idx = t, idx + i
        charge(cnt + 1, n_idx, arr[n_idx], n)


for t in range(int(input())):
    arr = list(map(int, input().split()))
    res, arr = arr[0], [0] + arr[1:]
    charge(0, 1, arr[1], res)
    print(f'#{t + 1} {res}')
