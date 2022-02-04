def rep(n):
    global tree

    while tree[n] != n:
        n = tree[n]

    return n


for t in range(int(input())):
    v, e = map(int, input().split())
    edge = sorted(
        [tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2]
    )

    tree, cnt, res = [i for i in range(v + 1)], 0, 0
    for p in edge:
        a, b = rep(p[0]), rep(p[1])
        if a != b:
            tree[b], res, cnt = a, res + p[2], cnt + 1
            if cnt == v:
                break

    print(f'#{t + 1} {res}')
