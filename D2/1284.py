for t in range(int(input())):
    p, q, r, s, w = map(int, input().split())
    print(f'#{t + 1} {min(p * w, q + max(w - r, 0) * s)}')
