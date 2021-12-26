for _ in range(10):
    t, arr = int(input()), list(map(int, input().split()))
    while arr[-1] != 0:
        for i in range(5):
            end = arr[0] - (i + 1)
            arr[0:7] = arr[1:]
            arr[-1] = end
            if arr[-1] <= 0:
                arr[-1] = 0
                break
    print(f'#{t} {" ".join(list(map(str, arr)))}')
