for t in range(int(input())):
    d, arr = int(input()), list(map(int, input().split()))

    res = 0
    while True:
        if arr:
            h = max(arr)
            idx = arr.index(h)
        else:
            break

        for i in arr[:idx]:
            res += h - i

        arr = arr[idx + 1:]

    print(f'#{t + 1} {res}')
