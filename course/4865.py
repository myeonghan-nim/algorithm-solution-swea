for t in range(int(input())):
    w, sen = input(), input()

    cnt, data = 0, set(w)
    for c in data:
        res = 0
        for raw in sen:
            if c == raw:
                res += 1
        cnt = max(cnt, res)

    print(f'#{t + 1} {cnt}')
