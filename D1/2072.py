for i in range(int(input())):
    print(f'#{i + 1} {sum([n for n in map(int, input().split()) if n % 2])}')
