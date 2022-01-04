def check(i, j):
    global d, n, cnt, mines, checked

    mines[i][j] = 0
    checked[i][j] = 1

    q = []
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if mines[ni][nj] == '*':
                return
            elif mines[ni][nj] == '.' and not checked[ni][nj]:
                q.append([ni, nj])

    for point in q:
        ni, nj = point
        check(ni, nj)
        mines[ni][nj] = 0


d = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
for t in range(int(input())):
    n = int(input())
    mines = [list(input()) for _ in range(n)]
    checked = [[0] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '.':
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if mines[ni][nj] == '*':
                            break
                else:
                    cnt += 1
                    check(i, j)

    for i in range(n):
        cnt += mines[i].count('.')

    print(f'#{t + 1} {cnt}')
