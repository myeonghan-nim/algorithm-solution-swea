for i in range(int(input())):
    a, b = map(int, input().split())
    print(f'#{i + 1} {">" if a > b else "<" if a < b else "="}')
