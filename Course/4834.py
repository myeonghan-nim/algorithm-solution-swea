for t in range(int(input())):
    _, arr = int(input()), input()

    cnt = [0] * 10
    for a in arr:
        cnt[int(a)] += 1

    n, idx = 0, 0
    for i in range(10):
        if n <= cnt[i]:
            n, idx = cnt[i], i

    print(f'#{t + 1} {idx} {n}')
