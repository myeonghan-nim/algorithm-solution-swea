for t in range(int(input())):
    _, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)

    res, cutted = 1, [(m, m)]
    for s in arr:
        side = 2 ** s
        for i in range(len(cutted)):
            w, h = cutted[i]
            if w >= side and h >= side:
                cutted.append((w - side, h - side))
                cutted.append((w - side, side))
                cutted.append((side, h - side))
                cutted = cutted[:i] + cutted[i + 1:]
                break
            elif i == len(cutted) - 1:
                res += 1
                cutted.append((m - side, m - side))
                cutted.append((m - side, side))
                cutted.append((side, m - side))

    print(f'#{t + 1} {res}')
