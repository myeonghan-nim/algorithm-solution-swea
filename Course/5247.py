def find(a, b):
    f, r = -1, -1
    q, check = [0] * 1000001, [0] * 1000001

    r += 1
    q[r] = a
    while f != r:
        f += 1
        n = q[f]

        if n == b:
            return check[n]
        else:
            for i in (n + 1, n - 1, n * 2, n - 10):
                if 1 <= i <= 1000000:
                    if not check[i]:
                        r += 1
                        q[r] = i
                        check[i] = check[n] + 1


for t in range(int(input())):
    n, m = map(int, input().split())
    print(f'#{t + 1} {find(n, m)}')
