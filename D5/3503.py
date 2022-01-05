for t in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)

    bat, idx, l, r = [arr[0]] * n, 1, 1, n - 1
    while l <= r:
        if idx % 2:
            bat[l] = arr[idx]
            l += 1
        else:
            bat[r] = arr[idx]
            r -= 1
        idx += 1

    res = 0
    for i in range(n):
        diff = abs(bat[i] - bat[i - 1])
        if res < diff:
            res = diff

    print(f'#{t + 1} {res}')
