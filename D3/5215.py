for t in range(int(input())):
    n, l = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    score = 0
    for i in range(1 << n):
        s, c = 0, 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j][0]
                c += arr[j][1]
            if c > l:
                break
        if c <= l:
            if score < s:
                score = s

    print(f'#{t + 1} {score}')
