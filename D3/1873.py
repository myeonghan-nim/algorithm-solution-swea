def shoot(h, w):
    global shape, mat

    for i in range(h):
        for j in range(w):
            if mat[i][j] in shape:
                ti, tj = i, j
                way = shape.index(mat[i][j])
                if way == 0:
                    while True:
                        ni = ti - 1
                        ti = ni
                        if 0 <= ni and mat[ni][tj] == '*':
                            mat[ni][tj] = '.'
                            return
                        elif ni < 0 or mat[ni][tj] == '#':
                            return
                elif way == 1:
                    while True:
                        ni = ti + 1
                        ti = ni
                        if ni < h and mat[ni][tj] == '*':
                            mat[ni][tj] = '.'
                            return
                        elif h <= ni or mat[ni][tj] == '#':
                            return
                elif way == 2:
                    while True:
                        nj = tj - 1
                        tj = nj
                        if 0 <= nj and mat[ti][nj] == '*':
                            mat[ti][nj] = '.'
                            return
                        elif nj < 0 or mat[ti][nj] == '#':
                            return
                else:
                    while True:
                        nj = tj + 1
                        tj = nj
                        if nj < w and mat[ti][nj] == '*':
                            mat[ti][nj] = '.'
                            return
                        elif w <= nj or mat[ti][nj] == '#':
                            return


def move(c, h, w):
    global shape, mat

    for i in range(h):
        for j in range(w):
            if mat[i][j] in shape:
                ti, tj = i, j
                if c == 'U':
                    mat[ti][tj] = '^'
                    ni = ti - 1
                    if 0 <= ni < h and mat[ni][tj] == '.':
                        mat[ni][tj], mat[ti][tj] = '^', '.'
                    return
                elif c == 'D':
                    mat[ti][tj] = 'v'
                    ni = ti + 1
                    if 0 <= ni < h and mat[ni][tj] == '.':
                        mat[ni][tj], mat[ti][tj] = 'v', '.'
                    return
                elif c == 'L':
                    mat[ti][tj] = '<'
                    nj = tj - 1
                    if 0 <= nj < w and mat[ti][nj] == '.':
                        mat[ti][nj], mat[ti][tj] = '<', '.'
                    return
                else:
                    mat[ti][tj] = '>'
                    nj = tj + 1
                    if 0 <= nj < w and mat[ti][nj] == '.':
                        mat[ti][nj], mat[ti][tj] = '>', '.'
                    return


shape = ['^', 'v', '<', '>']
for t in range(int(input())):
    h, w = map(int, input().split())
    mat = [list(input()) for _ in range(h)]

    n, commands = int(input()), input()
    for c in commands:
        if c == 'S':
            shoot(h, w)
        else:
            move(c, h, w)

    print(f'#{t + 1}', end=' ')
    for i in range(h):
        print(''.join(mat[i]))
