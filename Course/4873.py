for t in range(int(input())):
    arr = []
    for w in input():
        arr.append(w) if not arr or w != arr[-1] else arr.pop()
    print(f'#{t + 1} {len(arr)}')
