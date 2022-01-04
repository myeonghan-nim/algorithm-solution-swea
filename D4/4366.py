for t in range(int(input())):
    binary, ternary = list(input()), list(input())

    for i in range(len(binary)):
        binary[i] = str(1 - int(binary[i]))

        t_bin, t_ter, n = int(''.join(binary), 2), [], len(ternary) - 1
        while n >= -1:
            if t_bin // 3 ** n:
                t_ter += [str(t_bin // 3 ** n)]
                t_bin %= 3 ** n
            else:
                t_ter += ['0']
            n -= 1

        cnt = 0
        for j in range(len(ternary)):
            if ternary[j] != t_ter[j]:
                cnt += 1

        if cnt == 1:
            break

        binary[i] = str(1 - int(binary[i]))

    print(f'#{t + 1} {int("".join(binary), 2)}')
