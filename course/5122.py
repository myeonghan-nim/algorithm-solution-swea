def insert(arr, cmd):
    arr.insert(int(cmd[0]), int(cmd[1]))
    return arr


def delete(arr, cmd):
    return arr[:int(cmd[0])] + arr[int(cmd[0]) + 1:]


def change(arr, cmd):
    arr[int(cmd[0])] = int(cmd[1])
    return arr


function_dict = {'I': insert, 'D': delete, 'C': change}
for t in range(int(input())):
    _, m, l = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m):
        cmd = list(input().split())
        arr = function_dict[cmd[0]](arr, cmd[1:])

    res = -1
    if l <= len(arr):
        res = arr[l]

    print(f'#{t + 1} {res}')
