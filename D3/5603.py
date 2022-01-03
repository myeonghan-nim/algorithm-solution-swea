for t in range(int(input())):
    n = int(input())
    arr = [int(input()) for i in range(n)]

    avg, cnt = sum(arr) // n, 0
    for i in range(n):
        cnt += abs(avg - arr[i])

    print(f'#{t + 1} {cnt // 2}')
