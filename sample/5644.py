def charge(location_a, location_b):
    global n, arr, mat

    a, b = [], []
    for i in range(n):
        if location_a in mat[i]:
            a.append(i)
        if location_b in mat[i]:
            b.append(i)

    cnt, res = 0, 0
    if a and b:
        for i in a:
            for j in b:
                if i == j:
                    t = arr[i][3] // 2 + arr[j][3] // 2
                else:
                    t = arr[i][3] + arr[j][3]
                cnt = max(cnt, t)
        res += cnt
    else:
        for i in a:
            cnt = max(cnt, arr[i][3])
        res += cnt
        cnt = 0
        for i in b:
            cnt = max(cnt, arr[i][3])
        res += cnt

    return res


d = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
for t in range(int(input())):
    m, n = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    mat = [[] for _ in range(n)]
    for idx in range(n):
        for i in range(1, 11):
            for j in range(1, 11):
                cnt = abs(i - arr[idx][0]) + abs(j - arr[idx][1])
                if cnt <= arr[idx][2]:
                    mat[idx].append([i, j])

    p, q = [1, 1], [10, 10]
    res = charge(p, q)

    for idx in range(m):
        p = [p[0] + d[a[idx]][0], p[1] + d[a[idx]][1]]
        q = [q[0] + d[b[idx]][0], q[1] + d[b[idx]][1]]
        res += charge(p, q)

    print(f'#{t + 1} {res}')
