def pascal(i):
    res = []

    if not i:
        res.append('1')
    else:
        num, div = 1, 1
        for n in range(i + 1):
            if n == 0 or n == i:
                res.append('1')
            else:
                num *= i - n + 1
                div *= n
                res.append(f'{num // div}')

    return ' '.join(res)


for t in range(int(input())):
    print(f'#{t + 1}')
    for i in range(int(input())):
        print(pascal(i))
