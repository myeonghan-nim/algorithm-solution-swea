prime = [0, 0] + [1] * (10 ** 6 - 1)
for i in range(2, 10 ** 3 + 1):
    if prime[i]:
        for j in range(2 * i, 10 ** 6 + 1, i):
            prime[j] = 0

for i in range(len(prime)):
    if prime[i]:
        print(i, end=' ')
