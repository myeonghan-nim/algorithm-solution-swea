for t in range(int(input())):
    n = int(input())
    print(f'#{t + 1} {n * (n + 1) // 2} {2 * n * (n // 2) + (n if n % 2 else 0)} {(2 * n + 2) * (n // 2) + ((n + 1) if n % 2 else 0)}')
