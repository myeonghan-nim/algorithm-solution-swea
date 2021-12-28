for t in range(int(input())):
    a, b, c = input().split()
    print(f'#{t + 1} {c if a == b else a if b == c else b}')
