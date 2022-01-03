for t in range(int(input())):
    n = int(input())

    cnt, name = 0, 0
    print(f'#{t + 1}', end=' ')
    while True:
        word = input().split()
        for w in word:
            if w[-1] in '.!?':
                cnt += 1
                if w[:-1].isalpha():
                    if len(w) == 1 and w.isupper():
                        name += 1
                    elif w[0].isupper() and w[1:-1].islower():
                        name += 1
                print(name, end=' ')
                name = 0
            elif w.isalpha():
                if len(w) == 1 and w.isupper():
                    name += 1
                elif w[0].isupper() and w[1:].islower():
                    name += 1
        if cnt == n:
            break
    print()
