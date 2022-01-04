for t in range(int(input())):
    _, arr = int(input()), list(map(int, input().split()))

    checked, subsets = [1] + [0] * sum(arr), [0]
    for num in arr:
        queue = list(subsets)
        for n in queue:
            if not checked[n + num]:
                checked[n + num] = 1
                subsets += [n + num]

    print(f'#{t + 1} {sum(checked)}')
