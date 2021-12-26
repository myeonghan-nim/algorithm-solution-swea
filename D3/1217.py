def pow(n, m):
    return 1 if not m else n * pow(n, m - 1)


for _ in range(10):
    print(f'#{int(input())} {pow(*map(int, input().split()))}')
