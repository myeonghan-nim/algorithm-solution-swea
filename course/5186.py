for t in range(int(input())):
    n, res = float(input()), ''

    while n:
        n *= 2
        res, n = (res + '1', n - 1) if int(n) else (res + '0', n)
        if len(res) >= 13:
            res = 'overflow'
            break

    print(f'#{t + 1} {res}')
