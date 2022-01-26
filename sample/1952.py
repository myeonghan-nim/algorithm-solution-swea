def calculate(n, s):
    global daily, monthly, quaterly, table, res

    if n >= 13:
        res = min(s, res)
    else:
        calculate(n + 1, s + daily * table[n])
        calculate(n + 1, s + monthly)
        calculate(n + 3, s + quaterly)


for t in range(int(input())):
    daily, monthly, quaterly, yearly = map(int, input().split())
    table = [0] + list(map(int, input().split()))

    res = yearly
    calculate(1, 0)

    print(f'#{t + 1} {res}')
