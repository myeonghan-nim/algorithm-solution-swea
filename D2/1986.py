import math

for t in range(1, int(input()) + 1):
    res = math.ceil(t / 2)
    if not t % 2:
        res = -res
    print(f'#{t} {res}')
