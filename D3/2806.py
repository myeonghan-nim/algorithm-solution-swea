def queen(i, queens):
    global n, cnt, board

    if not queens:
        cnt += 1
    else:
        for j in range(n):
            is_exist = 0
            for moving in range(3):
                if not is_exist:
                    ti, tj = i + 1, j
                    while 0 <= ti < n and 0 <= tj < n:
                        if board[ti][tj]:
                            is_exist = 1
                            break
                        if moving == 0:
                            ti -= 1
                            tj -= 1
                        elif moving == 1:
                            ti -= 1
                        elif moving == 2:
                            ti -= 1
                            tj += 1
            if not is_exist:
                board[i + 1][j] = 1
                queen(i + 1, queens - 1)
                board[i + 1][j] = 0


for t in range(int(input())):
    n = int(input())

    cnt, board = 0, [[0] * n for _ in range(n)]
    for i in range(n):
        board[0][i] = 1
        queen(0, n - 1)
        board[0][i] = 0

    print(f'#{t + 1} {cnt}')
