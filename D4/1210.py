di, dj = [0, 0, 1], [1, -1, 0]

for _ in range(10):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    q, res = [], 0
    for j in range(100):
        if ladder[0][j] != 0:
            q.append([0, j])
            mirror = [[0] * 100 for _ in range(100)]
            while q:
                qi, qj = q.pop(0)
                for k in range(3):
                    ni, nj = qi + di[k], qj + dj[k]
                    if 0 <= ni < 100 and 0 <= nj < 100:
                        if ladder[ni][nj] == 1 and mirror[ni][nj] != 1:
                            q.append([ni, nj])
                            mirror[qi][qj] = 1
                            break
                        if ladder[ni][nj] == 2 and mirror[ni][nj] != 1:
                            res = j
                            break
        if res != 0:
            break

    print(f'#{n} {res}')
