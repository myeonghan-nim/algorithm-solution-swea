for t in range(int(input())):
    n, m, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n - 1):
        for j in range(n - m + 1):
            a, arr = 0, mat[i][j:j + m]
            for x in range(1, 2 ** m):
                h, cnt = 0, 0
                for y in range(m):
                    if x & (1 << y) and h + arr[y] <= c:
                        h += arr[y]
                        cnt += arr[y] ** 2
                a = max(a, cnt)

            for p in range(i + 1, n):
                for q in range(n - m + 1):
                    b, arr = 0, mat[p][q:q + m]
                    for x in range(1, 2 ** m):
                        h, cnt = 0, 0
                        for y in range(m):
                            if x & (1 << y) and h + arr[y] <= c:
                                h += arr[y]
                                cnt += arr[y] ** 2
                        b = max(b, cnt)

                    res = max(res, a + b)

    print(f'#{t + 1} {res}')
