for t in range(int(input())):
    n = int(input())

    num = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    while n != 1:
        for k in num:
            if not n % k:
                num[k] += 1
                n //= k

    print(f'#{t + 1} {" ".join(map(str, list(num.values())))}')
