for t in range(10):
    n, arr = int(input()), list(map(int, input().split()))

    cnt, i = 0, 2
    while i < n - 2:
        if arr[i] == max(arr[i - 2:i + 3]):
            part = sorted(arr[i - 2:i + 3])
            cnt += part[-1] - part[-2]
            i += 3
        else:
            i += 1

    print(f'#{t + 1} {cnt}')
