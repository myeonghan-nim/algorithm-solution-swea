for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(f'#{i + 1} {round(sum(arr) / len(arr))}')
