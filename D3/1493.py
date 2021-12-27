mat, n = [(0, 0)], 1
while n <= 285:
    i, j = 1, n
    for _ in range(n):
        mat.append((i, j))
        i += 1
        j -= 1
        if j <= 0:
            n += 1
            break

for t in range(int(input())):
    p, q = map(int, input().split())
    idx = mat.index((mat[p][0] + mat[q][0], mat[p][1] + mat[q][1]))
    print(f'#{t + 1} {idx}')
