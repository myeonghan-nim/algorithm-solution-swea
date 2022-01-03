for _ in range(int(input())):
    seq = input()

    n, mat = len(seq), [[]] * 5
    for i in range(5):
        if i in (0, 4):
            mat[i] = '..#' + '...#' * (n - 1) + '..'
        elif i in (1, 3):
            mat[i] = '.#' * 2 * n + '.'
        else:
            for s in seq:
                mat[i] += f'#.{s}.'
            mat[i] += '#'

    for i in range(5):
        print(''.join(mat[i]))
