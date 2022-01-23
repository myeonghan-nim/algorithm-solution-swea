for t in range(int(input())):
    arr = []
    for c in input():
        arr.append(c) if not arr or c != arr[-1] else arr.pop()
    print(f'#{t + 1} {len(arr)}')
