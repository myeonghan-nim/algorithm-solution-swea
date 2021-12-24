for t in range(int(input())):
    n = int(input())
    print(f'#{t + 1}', ' '.join(map(str, sorted(list(map(int, input().split()))))))
