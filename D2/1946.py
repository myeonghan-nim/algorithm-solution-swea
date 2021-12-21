import math

for t in range(int(input())):
    res = ''
    for i in range(int(input())):
        c, k = input().split()
        res += c * int(k)

    print(f'#{t + 1}')
    for i in range(math.ceil(len(res) / 10)):
        print(res[i * 10:(i + 1) * 10])
