def check(arr):
    global n, x

    s, e, c = 0, 0, [0] * n
    while True:
        e += 1
        if arr[s] != arr[e]:
            if abs(arr[s] - arr[e]) > 1:
                return 0
            else:
                for i in range(e, -1, -1):
                    if arr[i] != arr[e]:
                        s = i
                        break

                if arr[s] > arr[e]:
                    a, b = e, n - 1
                    for i in range(a, n):
                        if arr[i] != arr[a]:
                            b = i - 1
                            break

                    if b - a + 1 < x:
                        return 0
                    else:
                        if 1 in c[a:a + x]:
                            return 0
                        for i in range(a, a + x):
                            c[i] = 1
                        s, e = a, b
                else:
                    a, b = 0, s
                    for i in range(b, -1, -1):
                        if arr[i] != arr[b]:
                            a = i + 1
                            break

                    if b - a + 1 < x:
                        return 0
                    else:
                        if 1 in c[b - x + 1:b + 1]:
                            return 0
                        for i in range(b, b - x, -1):
                            c[i] = 1
                        s, e = e, s + 1

        if e == n - 1:
            return 1


for t in range(int(input())):
    n, x = map(int, input().split())
    row = [list(map(int, input().split())) for _ in range(n)]

    col = [[]] * n
    for i in range(n):
        arr = [0] * n
        for j in range(n):
            arr[j] = row[j][i]
        col[i] = arr[:]

    cnt = 0
    for i in range(n):
        cnt += check(row[i])
        cnt += check(col[i])

    print(f'#{t + 1} {cnt}')
