for t in range(int(input())):
    n, arr = int(input()), list(input().split())

    res = []
    if not n % 2:
        left, right = arr[:n // 2 + 1], arr[n // 2:]
        for i in range(n // 2):
            res.append(left[i])
            res.append(right[i])
    else:
        left, right = arr[:n // 2 + 1],  arr[n // 2 + 1:]
        for i in range(n // 2):
            res.append(left[i])
            res.append(right[i])
        res.append(left[-1])

    print(f'#{t + 1} {" ".join(res)}')
