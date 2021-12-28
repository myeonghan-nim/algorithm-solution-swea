for t in range(int(input())):
    n, arr = int(input()), []
    while len(arr) != n:
        arr += list(input().split())

    length = 0
    while True:
        collect, base = set(), set(range(10 ** length, 10 ** (length + 1)))
        if not length:
            base.add(0)

        for i in range(n - length):
            collect.add(int(''.join(arr[i:i + length + 1])))

        if base - collect:
            if len(str(min(base - collect))) == length + 1:
                break

        length += 1

    print(f'#{t + 1} {min(base - collect)}')
