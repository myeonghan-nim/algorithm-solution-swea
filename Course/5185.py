for t in range(int(input())):
    n, data = input().split()

    print(f'#{t + 1}', end=' ')
    for i in range(int(n)):
        num = ord(data[i])
        num -= ord('0') if data[i] in '0123456789' else ord('A') - 10
        for j in range(3, -1, -1):
            print('0', end='') if not num & (1 << j) else print('1', end='')
    print()
