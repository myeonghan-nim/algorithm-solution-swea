prime = [0, 0] + [1] * 999
for i in range(2, 1001):
    if prime[i]:
        n = 2 * i
        while n <= 1000:
            prime[n] = 0
            n += i


def find(i, n, t):
    global prime, cnt

    if t == 2:
        if i <= n and prime[n]:
            cnt += 1
    else:
        for idx in range(i, len(prime)):
            if prime[idx]:
                if idx <= n:
                    find(idx, n - idx, t + 1)


for t in range(int(input())):
    cnt = 0
    find(2, int(input()), 0)
    print(f'#{t + 1} {cnt}')
