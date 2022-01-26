for t in range(int(input())):
    k, n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [n]

    cnt, idx = 0, 0
    for i in range(1, m + 2):
        if arr[i] - arr[i - 1] > k:
            cnt = 0
            break
        elif arr[i] - arr[idx] > k:
            idx = i - 1
            cnt += 1

    print(f'#{t + 1} {cnt}')
