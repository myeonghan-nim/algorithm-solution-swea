for t in range(int(input())):
    n, cmd = input().split()

    n = int(n)
    tiles = [list(map(int, input().split())) for _ in range(n)]

    if cmd == 'up':
        for i in range(n):
            for j in range(n):
                if tiles[i][j] != 0:
                    ti = i
                    while True:
                        ti += 1
                        if ti >= n or (tiles[ti][j] != 0 and tiles[i][j] != tiles[ti][j]):
                            break
                        if tiles[i][j] == tiles[ti][j]:
                            tiles[i][j] *= 2
                            tiles[ti][j] = 0
                            break
                    ti = i
                    while True:
                        ti -= 1
                        if ti < 0 or tiles[ti][j] != 0:
                            tiles[i][j], tiles[ti +
                                               1][j] = tiles[ti + 1][j], tiles[i][j]
                            break
    elif cmd == 'down':
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if tiles[i][j] != 0:
                    ti = i
                    while True:
                        ti -= 1
                        if ti < 0 or (tiles[ti][j] != 0 and tiles[i][j] != tiles[ti][j]):
                            break
                        if tiles[i][j] == tiles[ti][j]:
                            tiles[i][j] *= 2
                            tiles[ti][j] = 0
                            break
                    ti = i
                    while True:
                        ti += 1
                        if ti >= n or tiles[ti][j] != 0:
                            tiles[i][j], tiles[ti -
                                               1][j] = tiles[ti - 1][j], tiles[i][j]
                            break
    elif cmd == 'left':
        for i in range(n):
            for j in range(n):
                if tiles[i][j] != 0:
                    tj = j
                    while True:
                        tj += 1
                        if tj >= n or (tiles[i][tj] != 0 and tiles[i][j] != tiles[i][tj]):
                            break
                        if tiles[i][j] == tiles[i][tj]:
                            tiles[i][j] *= 2
                            tiles[i][tj] = 0
                            break
                    tj = j
                    while True:
                        tj -= 1
                        if tj < 0 or tiles[i][tj] != 0:
                            tiles[i][j], tiles[i][tj +
                                                  1] = tiles[i][tj + 1], tiles[i][j]
                            break
    else:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if tiles[i][j] != 0:
                    tj = j
                    while True:
                        tj -= 1
                        if tj < 0 or (tiles[i][tj] != 0 and tiles[i][j] != tiles[i][tj]):
                            break
                        if tiles[i][j] == tiles[i][tj]:
                            tiles[i][j] *= 2
                            tiles[i][tj] = 0
                            break
                    tj = j
                    while True:
                        tj += 1
                        if tj >= n or tiles[i][tj] != 0:
                            tiles[i][j], tiles[i][tj -
                                                  1] = tiles[i][tj - 1], tiles[i][j]
                            break

    print(f'#{t + 1}')
    for i in range(n):
        print(' '.join(map(str, tiles[i])))
