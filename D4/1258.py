def find_box(n, mat):
    boxes = []

    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                s, e = [i, j], [i, j]

                while True:
                    ni = e[0] + 1
                    if ni < n and mat[ni][e[1]] != 0:
                        e[0] = ni
                    else:
                        break
                while True:
                    nj = e[1] + 1
                    if nj < n and mat[e[0]][nj] != 0:
                        e[1] = nj
                    else:
                        break

                for k in range(s[0], e[0] + 1):
                    mat[k][s[1]:e[1] + 1] = [0] * (e[1] - s[1] + 1)
                boxes.append((e[0] - s[0] + 1, e[1] - s[1] + 1))

    return boxes


for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    boxes = find_box(n, mat)
    boxes.sort(key=lambda box: (box[0] * box[1], box[0]))

    print(f'#{t + 1} {len(boxes)}', end=' ')
    for box in boxes:
        print(*box, end=' ')
    print()
