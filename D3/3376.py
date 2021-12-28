progress = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}


def p(n):
    global progress

    if n not in progress:
        progress[n] = p(n - 1) + p(n - 5)

    return progress[n]


for t in range(int(input())):
    print(f'#{t + 1} {p(int(input()))}')
