for T in range(int(input())):
    arr = sorted(list(map(int, input().split())))[1:-1]
    print(f'#{T + 1} {round(sum(arr) / len(arr))}')
