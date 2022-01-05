def find(n):
    global l, r, arr

    if n > 1:
        if n in l:
            idx = l.index(n)
        else:
            idx = r.index(n)
        arr.append(idx)
        find(idx)


def count(n, t):
    global l, r, cnt

    if n <= n:
        if l[n]:
            cnt += 1
            count(l[n], t)
        if r[n]:
            cnt += 1
            count(r[n], t)


for t in range(int(input())):
    v, e, a, b = map(int, input().split())
    nodes = list(map(int, input().split()))

    l, r = [0] * (v + 1), [0] * (v + 1)
    for i in range(0, 2 * e, 2):
        p, c = nodes[i], nodes[i + 1]
        if not l[p]:
            l[p] = c
        else:
            r[p] = c

    arr = []
    find(a)
    find(b)

    for i in range(len(arr)):
        if arr[i] in arr[i + 1:]:
            res = arr[i]
            break

    cnt = 1
    count(res, v)

    print(f'#{t + 1} {res} {cnt}')
