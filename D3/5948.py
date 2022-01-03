for t in range(int(input())):
    arr = list(map(int, input().split()))

    res = set()
    for i in range(7):
        s = arr[i]
        for j in range(i + 1, 7):
            s += arr[j]
            for k in range(j + 1, 7):
                s += arr[k]
                res.add(s)
                s -= arr[k]
            s -= arr[j]

    print(f'#{t + 1} {sorted(list(res), reverse=True)[4]}')
