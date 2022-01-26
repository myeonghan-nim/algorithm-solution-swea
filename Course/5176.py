def inorder(i, n):
    global tree, cnt

    if i <= n:
        inorder(i * 2, n)
        cnt += 1
        tree[i] = cnt
        inorder(i * 2 + 1, n)


for t in range(int(input())):
    n = int(input())
    tree, cnt = [0] * (n + 1), 0
    inorder(1, n)
    print(f'#{t + 1} {tree[1]} {tree[n // 2]}')
