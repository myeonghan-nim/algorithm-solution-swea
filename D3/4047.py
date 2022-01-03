for t in range(int(input())):
    cards = {k: 13 for k in ('S', 'D', 'H', 'C')}

    arr, count = input(), []
    while arr:
        count.append(arr[:3])
        arr = arr[3:]

    res = ''
    if len(count) != len(set(count)):
        res = 'ERROR'

    if res != 'ERROR':
        for c in count:
            cards[c[0]] -= 1
        res = str(cards['S']) + ' ' + str(cards['D']) + ' '
        res += str(cards['H']) + ' ' + str(cards['C'])

    print(f'#{t + 1} {res}')
