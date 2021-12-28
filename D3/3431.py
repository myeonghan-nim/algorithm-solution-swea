for t in range(int(input())):
    l, u, x = map(int, input().split())
    print(f'#{t + 1} {l - x if x < l else 0 if l <= x <= u else -1}')
