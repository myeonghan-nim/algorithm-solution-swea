for t in range(int(input())):
    _, arr = int(input()), list(map(int, input().split()))

    big, small = 0, 1000000
    for n in arr:
        big, small = max(big, n), min(small, n)

    print(f'#{t + 1} {big - small}')
