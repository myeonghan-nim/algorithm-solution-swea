for t in range(int(input())):
    w, sen = input(), input()

    res = 0
    while sen and not res:
        if sen[:len(w)][-1] in w:
            if sen[:len(w)][-1] == w[-1] and sen[:len(w)] == w:
                res = 1
            else:
                for i in range(len(w)):
                    if sen[i:i + len(w)] == w:
                        res = 1
        sen = sen[len(w):]

    print(f'#{t + 1} {res}')
