calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(int(input())):
    date = input()
    y, m, d = date[:4], date[4:6], date[6:]

    res = -1
    if 1 <= int(m) <= 12:
        if 1 <= int(d) <= calendar[int(m)]:
            res = f'{y}/{m}/{d}'

    print(f'#{i + 1} {res}')
