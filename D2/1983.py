rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for T in range(int(input())):
    n, k = map(int, input().split())

    arr = []
    for i in range(n):
        a, b, c = map(int, input().split())
        arr.append(a * 0.35 + b * 0.45 + c * 0.2)

    student = arr[k - 1]
    arr = sorted(arr, reverse=True)

    print(f'#{T + 1} {rank[arr.index(student) // (n // 10)]}')
