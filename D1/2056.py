days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(int(input())):
    date = input()
    year, month, day = date[:4], date[4:6], date[6:]

    res = -1
    if 1 <= int(month) <= 12:
        if 1 <= int(day) <= days[int(month)]:
            res = f'{year}/{month}/{day}'

    print(f'#{i + 1} {res}')
