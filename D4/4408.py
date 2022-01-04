for t in range(int(input())):
    n, rooms = int(input()), [0] * 201
    for _ in range(n):
        s, e = map(int, input().split())

        s = s // 2 + 1 if s % 2 else s // 2
        e = e // 2 + 1 if e % 2 else e // 2

        for i in range(min(s, e), max(s, e) + 1):
            rooms[i] += 1

    print(f'#{t + 1} {max(rooms)}')
