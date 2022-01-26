def find(n, i):
    global heap

    heap[i] = n
    while i // 2 >= 1 and heap[i // 2] > heap[i]:
        heap[i // 2], heap[i] = heap[i], heap[i // 2]
        i //= 2


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))

    i, heap = 0, [0] * (n + 1)
    for a in arr:
        i += 1
        find(a, i)

    res = 0
    while n // 2 >= 1:
        n //= 2
        res += heap[n]

    print(f'#{t + 1} {res}')
