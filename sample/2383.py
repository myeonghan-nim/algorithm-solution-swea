for t in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    res, people, stair = 100000, [], []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                people.append([i, j])
            elif mat[i][j] >= 2:
                stair.append([i, j, mat[i][j]])

    for i in range(1 << len(people)):
        a, b, d = [], [], [[] for _ in range(2)]
        for j in range(len(people)):
            d[0].append(j) if i & (1 << j) else d[1].append(j)
        for idx in d[0]:
            a.append(abs(people[idx][0] - stair[0][0]) +
                     abs(people[idx][1] - stair[0][1]))
        for idx in d[1]:
            b.append(abs(people[idx][0] - stair[1][0]) +
                     abs(people[idx][1] - stair[1][1]))

        a.sort()
        b.sort()
        stairs = [a, b]

        s, time = [[0] * 300 for _ in range(2)], [0] * 2
        for k in range(2):
            for m in range(len(d[k])):
                cnt, idx = stairs[k][m], 1
                while idx <= stair[k][2]:
                    if s[k][cnt + idx] >= 3 and idx == 1:
                        cnt += 1
                    elif s[k][cnt + idx] >= 3 and idx != 1:
                        c = 0
                        while s[k][cnt + idx + c] > 0:
                            c += 1
                        s[k][cnt + idx + c] += 1
                        idx += 1
                    elif s[k][cnt + idx] < 3:
                        s[k][cnt + idx] += 1
                        idx += 1

        for k in range(2):
            for m in range(len(s[k]) - 1, -1, -1):
                if s[k][m] != 0:
                    break
            time[k] = m + 1

        res = min(res, max(time))

    print(f'#{t + 1} {res}')
