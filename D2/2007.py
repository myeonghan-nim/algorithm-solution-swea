for t in range(int(input())):
    word, res = input().strip(), ''
    for c in word:
        if len(res) and res == word[len(res):len(res) * 2]:
            break
        res += c

    print(f'#{t + 1} {len(res)}')
