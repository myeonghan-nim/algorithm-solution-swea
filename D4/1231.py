def inorder(n, last):
    global tree, res

    if n <= last:
        inorder(n * 2, last)
        res += tree[n]
        inorder(n * 2 + 1, last)


for t in range(10):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]

    tree = [''] * (n + 1)
    for a in arr:
        tree[int(a[0])] = a[1]

    res = ''
    inorder(1, n)

    print(f'#{t + 1} {res}')
