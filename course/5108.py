for t in range(int(input())):
    _, m, l = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        idx, num = map(int, input().split())
        arr.insert(idx, num)

    print(f'#{t + 1} {arr[l]}')
