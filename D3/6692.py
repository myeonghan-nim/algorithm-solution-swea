for t in range(int(input())):
    n = int(input())
    boxes = [list(map(float, input().split())) for i in range(n)]

    res = 0
    for money in boxes:
        res += money[0] * money[1]

    print(f'#{t + 1} {res}')
