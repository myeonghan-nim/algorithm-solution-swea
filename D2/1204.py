for t in range(int(input())):
    n, score_dict = int(input()), {}
    for s in list(map(int, input().split())):
        score_dict[s] = score_dict[s] + 1 if s in score_dict else 1

    res, val = 0, 0
    for num, cnt in score_dict.items():
        if cnt > val:
            res, val = num, cnt
        elif cnt == val:
            if num > res:
                res = num

    print(f'#{n} {res}')
