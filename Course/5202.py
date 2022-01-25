for t in range(int(input())):
    n = int(input())
    schedule = sorted(
        [tuple(map(int, input().split())) for _ in range(n)], key=lambda s: s[1]
    )

    end, cnt = schedule[0][1], 1
    for s in schedule[1:]:
        if end <= s[0]:
            cnt += 1
            end = s[1]

    print(f'#{t + 1} {cnt}')
