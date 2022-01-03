for t in range(int(input())):
    d, a, b = map(int, input().split())

    d, arr = str(d), [0, 0] + [1] * (b - 1)
    for i in range(2, int(b ** 0.5) + 1):
        if arr[i]:
            for j in range(2 * i, b + 1, i):
                arr[j] = 0

    tenes = [i for i in range(a, b + 1) if arr[i] and d in str(i)]
    print(f'#{t + 1} {len(tenes)}')
