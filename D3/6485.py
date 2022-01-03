for t in range(int(input())):
    n = int(input())
    bus = [list(map(int, input().split())) for _ in range(n)]

    p = int(input())
    place = [int(input()) for _ in range(p)]

    arr = [0] + [0] * 5000
    for _ in range(n):
        s, e = bus.pop(0)
        for r in range(s, e + 1):
            arr[r] += 1

    res = ''
    for p in place:
        res += str(arr[p]) + ' '

    print(f'#{t + 1} {res}')
