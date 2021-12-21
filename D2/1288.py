nums = set(range(10))
for t in range(int(input())):
    s = n = int(input())

    cnt = set()
    while True:
        cnt |= set(int(i) for i in str(s))
        if nums == cnt:
            break
        s += n

    print(f'#{t + 1} {s}')
