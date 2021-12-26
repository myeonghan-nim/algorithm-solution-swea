def insert(password, command):
    left, right = password[:int(command[1])], password[int(command[1]):]
    return left + command[3:] + right


for t in range(10):
    n, password = int(input()), list(input().split())
    c, commands = int(input()), list(input().split())

    while commands:
        command = commands[:int(commands[2]) + 3]
        commands = commands[len(command):]
        password = insert(password, command)

    print(f'#{t + 1} {" ".join(password[:10])}')
