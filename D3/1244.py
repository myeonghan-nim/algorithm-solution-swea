def find(n, k, c):
    global res, cnt, card

    if not c or n == k:
        s = 0
        for i in range(k):
            s = s * 10 + int(card[i])
        if res <= s:
            res = s
            if cnt > c:
                cnt = c
    else:
        for i in range(k):
            card[n], card[i] = card[i], card[n]
            is_moved = 1 if n != i else 0
            find(n + 1, k, c - is_moved)
            card[n], card[i] = card[i], card[n]


for t in range(int(input())):
    card, n = input().split()

    card, res, cnt = list(card), 0, int(n)
    for i in range(len(card)):
        res = res * 10 + int(card[i])

    find(0, len(card), cnt)
    if cnt % 2:
        res = (res // 100) * 100 + (res % 10) * 10 + (res % 100) // 10

    print(f'#{t + 1} {res}')
