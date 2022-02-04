def find(i, n):
    global heap

    if i <= n:
        if heap[i]:
            return heap[i]
        return find(i * 2, n) + find(i * 2 + 1, n)
    else:
        return 0


for t in range(int(input())):
    n, m, l = map(int, input().split())

    heap = [0] * (n + 1)
    for _ in range(m):
        idx, num = map(int, input().split())
        heap[idx] = num

    for i in range(n, 0, -1):
        if not heap[i]:
            heap[i] = find(i, n)

    print(f'#{t + 1} {heap[l]}')
