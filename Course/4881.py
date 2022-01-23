def npr(i, k, s):
    global n, mat, res, used

    if s > res:
        return

    if i == k:
        res = min(s, res)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = 1
                npr(i + 1, k, s + mat[i][j])
                used[j] = 0


for t in range(int(input())):
    n = int(input())
    mat, used = [list(map(int, input().split())) for _ in range(n)], [0] * n

    res = 0
    for i in range(n):
        res += sum(mat[i])

    npr(0, n, 0)
    print(f'#{t + 1} {res}')
