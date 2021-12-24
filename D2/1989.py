for t in range(int(input())):
    word = input()
    res = 1 if word == word[::-1] else 0
    print(f'#{t + 1} {res}')
