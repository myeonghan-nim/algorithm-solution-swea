for t in range(int(input())):
    n, e = map(int, input().split())

    nodes = [0] + [10 ** n] * n
    for _ in range(e):
        a, b, l = map(int, input().split())
        nodes[b] = min(nodes[b], nodes[a] + l)

    print(f'#{t + 1} {nodes[n]}')
