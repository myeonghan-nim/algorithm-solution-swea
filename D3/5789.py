for t in range(int(input())):
    n, q = map(int, input().split())

    boxes = [0] * n
    for idx in range(q):
        l, r = map(int, input().split())
        boxes[l - 1:r] = [idx + 1] * (r + 1 - l)

    print(f'#{t + 1} {" ".join(map(str, boxes))}')
