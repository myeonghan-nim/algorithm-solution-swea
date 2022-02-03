for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    big, small = 0, 10000 * m
    for i in range(n - m + 1):
        big, small = max(big, sum(arr[i:i + m])), min(small, sum(arr[i:i + m]))

    print(f'#{t + 1} {big - small}')
