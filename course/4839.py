def check(p, n):
    l, r, c, cnt = 1, p, (1 + p) // 2, 0
    while l < r:
        if n != c:
            if n > c:
                l = c
            else:
                r = c
            c = (l + r) // 2
            cnt += 1
        else:
            return cnt


for t in range(int(input())):
    p, a, b = map(int, input().split())
    x, y = check(p, a), check(p, b)
    res = 'B' if x > y else 'A' if x < y else 0
    print(f'#{t + 1} {res}')
