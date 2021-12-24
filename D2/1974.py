def sudoku(mat):
    ans = set(range(1, 10))

    for i in range(9):
        row, col = set(), set()
        for j in range(9):
            row.add(mat[i][j])
            col.add(mat[j][i])
        if row != ans or col != ans:
            return 0

    for m in range(3):
        for n in range(3):
            p, box = (3 * m, 3 * n), set()
            for i in range(p[0], p[0] + 3):
                for j in range(p[1], p[1] + 3):
                    box.add(mat[i][j])
            if box != ans:
                return 0

    return 1


for t in range(int(input())):
    print(
        f'#{t + 1} {sudoku([list(map(int, input().split())) for _ in range(9)])}')
