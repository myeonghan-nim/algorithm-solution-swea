cad = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(int(input())):
    arr = list(map(int, input().split()))

    day = cad[arr[0]] - arr[1] + 1
    if arr[0] != arr[2]:
        day += sum(cad[(arr[0] + 1):arr[2]]) + arr[3]

    print(f'#{t + 1} {day}')
