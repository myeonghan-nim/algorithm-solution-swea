code = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'
}

for t in range(int(input())):
    n, m = map(int, input().split())
    mat = [input() for _ in range(n)]

    for i in range(n):
        if mat[i] != '0' * m:
            secret = mat[i]
            break

    idx = m - 1
    while idx >= 0:
        if secret[idx] != '0':
            secret = secret[idx - 55:idx + 1]
            break
        else:
            idx -= 1

    res = ''
    while secret:
        res += code.get(secret[:7])
        secret = secret[7:]

    check = num = 0
    for i in range(len(res)):
        check += 3 * int(res[i]) if not i % 2 else int(res[i])

    if not check % 10:
        for r in res:
            num += int(r)

    print(f'#{t + 1} {num}')
