def calc(n, last):
    global tree

    if n <= last:
        if type(tree[n]) == tuple:
            op, n1, n2 = tree[n][0], int(tree[n][1]), int(tree[n][2])

            calc(n1, last)
            calc(n2, last)

            if op == '+':
                tree[n] = tree[n1] + tree[n2]
            elif op == '-':
                tree[n] = tree[n1] - tree[n2]
            elif op == '*':
                tree[n] = tree[n1] * tree[n2]
            elif op == '/':
                tree[n] = tree[n1] / tree[n2]


for t in range(10):
    n = int(input())

    tree = [0] * (n + 1)
    for _ in range(n):
        info = input().split()
        if info[1].isdigit():
            tree[int(info[0])] = int(info[1])
        else:
            tree[int(info[0])] = (info[1], info[2], info[3])

    calc(1, n)

    print(f'#{t + 1} {int(tree[1])}')
