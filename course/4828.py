for t in range(int(input())):
    _, arr = int(input()), list(map(int, input().split()))

    b, s = 0, 1000000
    for n in arr:
        b, s = max(b, n), min(s, n)

    print(f'#{t + 1} {b - s}')
