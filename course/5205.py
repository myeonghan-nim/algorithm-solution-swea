def partition(arr, left, right):
    p, i = arr[right], left - 1
    for j in range(left, right):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        idx = partition(arr, left, right)
        quick_sort(arr, left, idx - 1)
        quick_sort(arr, idx + 1, right)
    return arr


for t in range(int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    print(f'#{t + 1} {quick_sort(arr, 0, n - 1)[n // 2]}')
