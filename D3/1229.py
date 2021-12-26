def insert(password, command):
    left, right = password[:int(command[1])], password[int(command[1]):]
    return left + command[3:] + right


def delete(password, command):
    left = password[:int(command[1])]
    right = password[int(command[1]) + int(command[2]):]
    return left + right


for t in range(10):
    n, password = int(input()), list(input().split())
    c, commands = int(input()), list(input().split())

    while commands:
        cmd = commands[0]
        if cmd == 'I':
            command = commands[:int(commands[2]) + 3]
            commands = commands[len(command):]
            new = insert(password, command)
        elif cmd == 'D':
            command = commands[:3]
            commands = commands[len(command):]
            new = delete(password, command)
        password = new

    print(f'#{t + 1} {" ".join(password[:10])}')
