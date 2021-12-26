for _ in range(10):
    t = int(input())
    mat = [list(input()) for i in range(100)]

    rev = [[0 for i in range(100)] for i in range(100)]
    for i in range(100):
        for j in range(100):
            rev[j][i] = mat[i][j]

    l = 0
    for n in range(100):
        start, end = 1, 100
        while end > 0:
            for data in (mat, rev):
                for i in range(start):
                    if data[n][i:end + i] == data[n][i:end + i][::-1]:
                        if len(data[n][i:end + i]) > l:
                            l = len(data[n][i:end + i])
                            break
            start += 1
            end -= 1

    print(f'#{t} {l}')
