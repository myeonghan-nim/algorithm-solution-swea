for t in range(int(input())):
    people = list(map(int, input()))

    c, res = 0, 0
    for i in range(len(people)):
        if c < i:
            res += i - c
            c += i - c
        c += people[i]

    print(f'#{t + 1} {res}')
