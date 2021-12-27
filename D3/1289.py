for t in range(int(input())):
    org = input()
    err = list('0' * len(org))

    cnt, idx = 0, 0
    for o in org:
        if o != err[idx]:
            err[idx:] = o * (len(org) - idx)
            cnt += 1
        idx += 1

    print(f'#{t + 1} {cnt}')
