for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input())) for i in range(n)]

    mid, res = n // 2, 0
    for i in range(n):
        if i < mid:
            res += sum(mat[i][mid - i:mid + i + 1])
        else:
            res += sum(mat[i][mid - (n - i - 1):mid + (n - i)])

    print(f'#{t + 1} {res}')
