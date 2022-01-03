for t in range(int(input())):
    seq = list(input())
    rev = seq[::-1]

    res = 'Exist'
    if seq != rev:
        for i in range(len(seq) // 2):
            if seq[i] != rev[i]:
                if seq[i] != '?' and rev[i] != '?':
                    res = 'Not exist'
                    break

    print(f'#{t + 1} {res}')
