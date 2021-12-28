for t in range(int(input())):
    arr, res = list(map(int, input().split())), 0
    for n in arr:
        res += n if n >= 40 else 40
    print(f'#{t + 1} {res // 5}')
