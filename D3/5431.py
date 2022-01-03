for t in range(int(input())):
    n, _ = map(int, input().split())
    arr = set(map(int, input().split()))
    print(f'#{t + 1} {" ".join(map(str, sorted(list(set(range(1, n + 1)) - arr))))}')
