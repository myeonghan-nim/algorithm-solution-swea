for t in range(int(input())):
    word, sentence = input(), input()

    cnt, word_set = 0, set(word)
    for w in word_set:
        res = 0
        for s in sentence:
            if w == s:
                res += 1
        cnt = max(cnt, res)

    print(f'#{t + 1} {cnt}')
