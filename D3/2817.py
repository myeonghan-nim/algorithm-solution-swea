for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(1 << n):
        sample = 0
        for j in range(n):
            if i & (1 << j):
                sample += arr[j]
                if sample > k:
                    break
        if sample == k:
            res += 1

    print(f'#{t + 1} {res}')
