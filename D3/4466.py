for t in range(int(input())):
    _, k = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{t + 1} {sum(scores[:k])}')
