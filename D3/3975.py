case = int(input())

idx, res = 0, [''] * case
for _ in range(case):
    a, b, c, d = map(int, input().split())
    res[idx] = 'ALICE' if a / b > c / d else 'BOB' if a / b < c / d else 'DRAW'
    idx += 1

for i in range(case):
    print(f'#{i + 1} {res[i]}')
