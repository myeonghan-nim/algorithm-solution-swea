for t in range(int(input())):
    n, m = map(int, input().split())
    print(f'#{t + 1} {len(set(input().split()) & set(input().split()))}')
