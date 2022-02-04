for t in range(int(input())):
    _ = input()
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = list(map(int, input().split()))

    res = 0
    for truck in trucks:
        for container in containers:
            if truck >= container:
                res += container
                containers = containers[:containers.index(container)]
                containers += containers[containers.index(container) + 1:]
                break

    print(f'#{t + 1} {res}')
