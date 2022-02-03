def combination(n, r):
    global k, cnt, arr, number

    if not r:
        if sum(arr) == k:
            cnt += 1
    elif r > n:
        return
    else:
        arr[r - 1] = number[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)


for t in range(int(input())):
    n, k = map(int, input().split())
    cnt, arr, number = 0, [0] * n, list(range(1, 13))
    combination(12, n)
    print(f'#{t + 1} {cnt}')
