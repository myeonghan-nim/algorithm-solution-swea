num = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
    'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
}
rev = {v: k for k, v in num.items()}

for _ in range(int(input())):
    t, n = map(str, input().split())
    n = int(n)

    arr = list(input().split())
    for i in range(n):
        arr[i] = num[arr[i]]

    arr = sorted(arr)
    for i in range(n):
        arr[i] = rev[arr[i]]

    print(t)
    print(' '.join(arr))
