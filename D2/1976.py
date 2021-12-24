for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(f'#{t + 1} {(a + c) % 12 + (b + d) // 60} {(b + d) % 60}')
