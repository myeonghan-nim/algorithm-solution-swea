for t in range(int(input())):
    word, sentence = input(), input()

    res = 0
    while sentence and not res:
        if sentence[:len(word)][-1] in word:
            if sentence[:len(word)][-1] == word[-1] and sentence[:len(word)] == word:
                res = 1
            else:
                for i in range(len(word)):
                    if sentence[i:i + len(word)] == word:
                        res = 1
        sentence = sentence[len(word):]

    print(f'#{t + 1} {res}')
