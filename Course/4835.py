for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    b, s = 0, 10000 * m
    for i in range(n - m + 1):
        b, s = max(b, sum(arr[i:i + m])), min(s, sum(arr[i:i + m]))

    print(f'#{t + 1} {b - s}')
