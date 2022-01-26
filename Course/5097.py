for t in range(int(input())):
    _, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m):
        arr.append(arr.pop(0))

    print(f'#{t + 1} {arr[0]}')
