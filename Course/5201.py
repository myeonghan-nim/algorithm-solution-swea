for t in range(int(input())):
    _, _ = map(int, input().split())
    cs = sorted(list(map(int, input().split())), reverse=True)
    vs = list(map(int, input().split()))

    res = 0
    for v in vs:
        for c in cs:
            if v >= c:
                res += c
                cs = cs[:cs.index(c)] + cs[cs.index(c) + 1:]
                break

    print(f'#{t + 1} {res}')
