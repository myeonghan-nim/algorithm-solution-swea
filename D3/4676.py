for t in range(int(input())):
    seq, h = input(), int(input())
    arr = list(map(int, input().split()))

    ins = [''] * (len(seq) + 1)
    for _ in range(h):
        ins[arr.pop(0)] += '-'

    res = ''
    for i in range(len(ins)):
        res += ins[i] + seq[i] if i < len(ins) - 1 else ins[i]

    print(f'#{t + 1} {res}')
