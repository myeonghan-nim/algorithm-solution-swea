arr = [0, 1, 3]
for i in range(3, 301):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

for t in range(int(input())):
    n = int(input()) // 10
    print(f'#{t + 1} {arr[n]}')
