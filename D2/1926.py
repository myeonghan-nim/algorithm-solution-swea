for n in range(1, int(input()) + 1):
    res = n
    if '3' in str(n) or '6' in str(n) or '9' in str(n):
        res = '-' * (str(n).count('3') + str(n).count('6') + str(n).count('9'))
    print(res, end=' ')
