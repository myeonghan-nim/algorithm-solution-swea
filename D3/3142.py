for t in range(int(input())):
    n, m = map(int, input().split())
    print(f'#{t + 1} {2 * m - n} {m - (2 * m - n)}')
