for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(input())

    res = set()
    for _ in range(n // 4):
        for j in range(0, len(arr), n // 4):
            res.add(''.join(arr[j:j + n // 4]))
        arr = arr[1:] + [arr[0]]

    print(f'#{t + 1} {int(sorted(list(res), reverse=True)[k - 1], 16)}')
