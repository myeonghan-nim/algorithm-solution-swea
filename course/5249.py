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

    tree, cnt, s = [i for i in range(v + 1)], 0, 0
    for e in edge:
        a, b = rep(e[0]), rep(e[1])
        if a != b:
            tree[b] = a
            s += e[2]
            cnt += 1
            if cnt == v:
                break

    print(f'#{t + 1} {s}')
