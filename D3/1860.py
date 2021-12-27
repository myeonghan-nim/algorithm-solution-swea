for t in range(int(input())):
    n, m, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    res = 'Possible'
    for i in range(n):
        bread = (arr[i] // m) * k - i
        if bread <= 0:
            res = 'Impossible'
            break

    print(f'#{t + 1} {res}')
