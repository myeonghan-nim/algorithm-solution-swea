for t in range(int(input())):
    _, m = map(int, input().split())

    res = []
    for _ in range(m):
        arr = list(map(int, input().split()))
        if not res:
            res = arr[:]
        else:
            for i in range(len(res)):
                if res[i] > arr[0]:
                    res[i:i] = arr
                    break
            else:
                res += arr

    print(f'#{t + 1} {" ".join(map(str, res[::-1][:10]))}')
