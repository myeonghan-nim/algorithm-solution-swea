def check(data):
    arr = []
    for d in data:
        if d in '({':
            arr.append(d)
        elif d == ')' and (not arr or arr.pop() != '('):
            return 0
        elif d == '}' and (not arr or arr.pop() != '{'):
            return 0
    return int(not arr)


for t in range(int(input())):
    print(f'#{t + 1} {check(input())}')
