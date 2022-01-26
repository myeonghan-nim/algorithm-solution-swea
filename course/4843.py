def special_sort(idx, n):
    global arr

    t = idx

    if not idx % 2:
        for i in range(idx + 1, n):
            if arr[idx] < arr[i]:
                idx = i
    else:
        for i in range(idx + 1, n):
            if arr[idx] > arr[i]:
                idx = i

    arr[t], arr[idx] = arr[idx], arr[t]


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    for i in range(n):
        special_sort(i, n)
    print(f'#{t + 1} {" ".join(map(str, arr[:10]))}')
