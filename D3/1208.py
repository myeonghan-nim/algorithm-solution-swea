for t in range(10):
    n, arr = int(input()), list(map(int, input().split()))
    for i in range(n):
        max_idx, min_idx = arr.index(max(arr)), arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1
    print(f'#{t + 1} {max(arr) - min(arr)}')
