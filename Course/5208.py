def charge(cnt, idx, length, n):
    global arr, res

    if length + idx >= n:
        res = min(res, cnt)
    else:
        max_length, next_idx = 0, 0
        for i in range(1, length + 1):
            t = idx + i + arr[idx + i]
            if max_length < t:
                max_length, next_idx = t, idx + i
        charge(cnt + 1, next_idx, arr[next_idx], n)


for t in range(int(input())):
    arr = list(map(int, input().split()))
    res, arr = arr[0], [0] + arr[1:]
    charge(0, 1, arr[1], res)
    print(f'#{t + 1} {res}')
