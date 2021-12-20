for i in range(int(input())):
    a, b = map(int, input().split())
    res = '>' if a > b else '<' if a < b else '='
    print(f'#{i + 1} {res}')
