def check(arr):
    idx = [0] * 10

    for n in arr:
        idx[n] += 1

    for i in range(1, 9):
        if idx[i - 1] >= 3 or idx[i] >= 3 or idx[i + 1] >= 3:
            return 1
        if idx[i - 1] >= 1 and idx[i] >= 1 and idx[i + 1] >= 1:
            return 1

    return 0


for t in range(int(input())):
    arr = list(map(int, input().split()))

    a, b, m, n, res = [], [], 0, 0, 0
    for i in range(12):
        if not i % 2:
            a.append(arr[i])
            m = check(a)
        else:
            b.append(arr[i])
            n = check(b)

        if m and not n:
            res = 1
            break
        elif n and not m:
            res = 2
            break

    print(f'#{t + 1} {res}')
