for t in range(int(input())):
    n = int(input())
    days = list(int(input()) for _ in range(n))

    for i in days[1:]:
        for j in range(2 * i - 1, days[-1] + 1, i - 1):
            if j in days:
                days.remove(j)

    print(f'#{t + 1} {len(days[1:])}')
