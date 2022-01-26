def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    res = [0] * (len(left) + len(right))
    i, j, idx = 0, 0, 0
    while True:
        if i <= len(left) - 1 and j <= len(right) - 1:
            if left[i] <= right[j]:
                res[idx] = left[i]
                i += 1
            else:
                res[idx] = right[j]
                j += 1
        elif i <= len(left) - 1:
            res[idx] = left[i]
            i += 1
        else:
            res[idx] = right[j]
            j += 1

        idx += 1
        if i >= len(left) and j >= len(right):
            return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    cnt = 0
    print(f'#{t + 1} {merge_sort(arr)[n // 2]} {cnt}')
