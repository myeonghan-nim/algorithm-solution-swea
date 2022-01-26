for t in range(int(input())):
    _, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    idx = 0
    for i in range(k):
        idx += m
        if idx > len(arr):
            idx %= len(arr)
        arr.insert(idx, arr[idx - 1] + arr[idx % len(arr)])

    print(f'#{t + 1} {" ".join(map(str, arr[::-1][:10]))}')
