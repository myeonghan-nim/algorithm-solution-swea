for t in range(int(input())):
    d, h, m = map(int, input().split())
    print(f'#{t + 1} {max((d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11), -1)}')
