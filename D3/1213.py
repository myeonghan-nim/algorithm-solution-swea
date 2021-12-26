for _ in range(10):
    t, search, sentence = int(input()), input(), input()

    cnt, i = 0, 0
    while i <= len(sentence):
        if search == sentence[i:i + len(search)]:
            cnt += 1
            i += len(search)
        i += 1

    print(f'#{t} {cnt}')
