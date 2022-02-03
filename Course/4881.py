def permutation(i, k, s):
    global n, mat, res, used

    if s > res:
        return

    if i == k:
        res = min(s, res)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = 1
                permutation(i + 1, k, s + mat[i][j])
                used[j] = 0


for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res, used = 0, [0] * n
    for i in range(n):
        res += sum(mat[i])

    permutation(0, n, 0)
    print(f'#{t + 1} {res}')
