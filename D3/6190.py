for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))

    res = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = str(arr[i] * arr[j])
            if len(s) != 1:
                for l in range(len(s) - 1):
                    if int(s[l]) > int(s[l + 1]):
                        break
                else:
                    if res < int(s):
                        res = int(s)

    print(f'#{t + 1} {res}')
