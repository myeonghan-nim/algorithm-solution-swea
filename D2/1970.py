from collections import OrderedDict

for t in range(int(input())):
    n = int(input())
    money = OrderedDict(
        {k: 0 for k in [50000, 10000, 5000, 1000, 500, 100, 50, 10]})

    while n >= 10:
        for k, _ in money.items():
            if n >= k:
                n -= k
                money[k] += 1
                break

    print(f'#{t + 1}')
    print(' '.join(map(str, money.values())))
