for t in range(int(input())):
    n, _ = map(int, input().split())
    pizza = list(map(int, input().split()))

    q, arr, i = [], [], 1
    while True:
        if len(q) != n and pizza:
            q.append(pizza[0])
            arr.append(i)
            pizza = pizza[1:]
            i += 1
        else:
            p, idx = q.pop(0), arr.pop(0)
            if p // 2:
                q.append(p // 2)
                arr.append(idx)
            if len(q) == 1:
                break

    print(f'#{t + 1} {arr[0]}')
