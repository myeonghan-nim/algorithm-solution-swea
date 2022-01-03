days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(int(input())):
    m, d = map(int, input().split())

    res = (sum(days[:m]) + d) % 7 + 3
    if res >= 7:
        res -= 7

    print(f'#{t + 1} {res}')
