for t in range(int(input())):
    row, v, l = int(input()), 0, 0
    for r in range(row):
        arr = list(map(int, input().split()))
        if len(arr) != 1:
            cmd, a = arr[0], arr[1]
            v += a if cmd == 1 else -a
            if v < 0:
                v = 0
        l += v

    print(f'#{t + 1} {l}')
