for t in range(int(input())):
    res, arr = '', []
    for cmd in list(input().split()):
        if cmd in '+-*/.':
            if cmd == '.':
                res = 'error' if len(arr) > 1 else arr.pop()
                break
            else:
                if len(arr) < 2:
                    res = 'error'
                    break
                b, a = arr.pop(), arr.pop()
                if cmd == '+':
                    arr.append(a + b)
                elif cmd == '-':
                    arr.append(a - b)
                elif cmd == '*':
                    arr.append(a * b)
                elif cmd == '/':
                    arr.append(a // b)
        else:
            arr.append(int(cmd))

    print(f'#{t + 1} {res}')
