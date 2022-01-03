vowels = ['a', 'e', 'i', 'o', 'u']
for t in range(int(input())):
    print(f'#{t + 1} {"".join([s for s in input() if s not in vowels])}')
