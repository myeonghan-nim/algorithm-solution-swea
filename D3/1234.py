def password(pwd):
    arr = []
    for p in pwd:
        if not arr or arr[-1] != p:
            arr.append(p)
        elif arr[-1] == p:
            arr.pop()
    return ''.join(arr)


for t in range(10):
    n, pwd = input().split()
    print(f'#{t + 1} {password(pwd)}')
