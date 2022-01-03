for t in range(int(input())):
    a, b, c = map(int, input().split())
    print(f'#{t + 1} {max(c // a, c // b)}')
