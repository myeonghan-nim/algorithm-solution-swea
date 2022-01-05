def f(n, m, arr):
    used, res = [[0] * (4 * m) for _ in range(n)], 0

    for i in range(n):
        j = 4 * m - 1
        while j > 0:
            if arr[i][j] == '1' and not used[i][j]:
                pwd, col = [0] * 8, j
                for k in range(7, -1, -1):
                    cnt = [0, 0, 0]
                    while arr[i][col] == '0':
                        col -= 1
                    while arr[i][col] == '1':
                        cnt[0] += 1
                        col -= 1
                    while arr[i][col] == '0':
                        cnt[1] += 1
                        col -= 1
                    while arr[i][col] == '1':
                        cnt[2] += 1
                        col -= 1

                    cnt = [c // min(cnt) for c in cnt]
                    idx = cnt[0] * 100 + cnt[1] * 10 + cnt[2]
                    pwd[k] = pattern.index(idx)

                c = (pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3
                c += pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if not c % 10:
                    res += sum(pwd)

                r = i
                while arr[r][j] == '1':
                    for k in range(col + 1, j + 1):
                        used[r][k] = 1
                    r += 1
                j = col
            else:
                j -= 1

    return res


pattern = [112, 122, 221, 114, 231, 132, 411, 213, 312, 211]
hexer = ['0000', '0001', '0010', '0011',
         '0100', '0101', '0110', '0111',
         '1000', '1001', '1010', '1011',
         '1100', '1101', '1110', '1111']

for t in range(int(input())):
    n, m = map(int, input().split())
    code, arr = [input() for _ in range(n)], [''] * n
    for i in range(n):
        for j in range(m):
            arr[i] += hexer[int(code[i][j], 16)]
    print(f'#{t + 1} {f(n, m, arr)}')
