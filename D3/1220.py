def magnetic(mat):
    cnt = 0
    for i in range(100):
        sentence = ''
        for j in range(100):
            if mat[j][i] != '0':
                sentence += mat[j][i]
        cnt += sentence.count('12')
    return cnt


for t in range(10):
    n = int(input())
    print(f'#{t + 1} {magnetic([input().split() for _ in range(n)])}')
