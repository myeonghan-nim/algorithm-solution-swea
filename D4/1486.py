for t in range(int(input())):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))

    res = sum(arr)
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
        if s >= b:
            if res > s:
                res = s

    print(f'#{t + 1} {res - b}')
