arr = [0, 1, 3]
for i in range(3, 301):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

for t in range(int(input())):
    print(f'#{t + 1} {arr[int(input()) // 10]}')
