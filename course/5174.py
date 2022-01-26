def inorder(n):
    global a, b, cnt

    if n > 0:
        inorder(a[n])
        cnt += 1
        inorder(b[n])


for t in range(int(input())):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))

    a, b = [0] * (e + 2), [0] * (e + 2)
    for i in range(e):
        p, c = arr[2 * i], arr[2 * i + 1]

        if not a[p]:
            a[p] = c
        else:
            b[p] = c

    cnt = 0
    inorder(n)

    print(f'#{t + 1} {cnt}')
