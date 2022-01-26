class Micro:
    def __init__(self, x, y, num, direction):
        self.x, self.y = x, y
        self.num, self.direction = num, direction
        self.is_dead = False

    def change_direction(self):
        if self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 4
        elif self.direction == 4:
            self.direction = 3

    def cut(self):
        self.num //= 2
        if not self.num:
            self.is_dead = True

    def move(self, n):
        if self.direction == 1:
            self.x -= 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y -= 1
        elif self.direction == 4:
            self.y += 1

        if self.x in (0, n - 1) or self.y in (0, n - 1):
            self.change_direction()
            self.cut()

        return self.x, self.y


def meet(micros):
    res, m, b = 0, 0, micros[0]
    for micro in micros:
        res += micro.num
        if micro.num > m:
            m, b = micro.num, micro

    b.num = res
    for micro in micros:
        if micro != b:
            micro.is_dead = True


for t in range(int(input())):
    n, m, k = map(int, input().split())

    micros = []
    for _ in range(k):
        micros.append(Micro(*list(map(int, input().split()))))

    h = 0
    while h < m:
        h += 1

        mat = {}
        for micro in micros:
            if not micro.is_dead:
                p = micro.move(n)
                if p in mat:
                    mat[p].append(micro)
                else:
                    mat[p] = [micro]

        for p in mat:
            group = mat[p]
            if len(group) >= 2:
                meet(group)

    res = 0
    for micro in micros:
        if not micro.is_dead:
            res += micro.num

    print(f'#{t + 1} {res}')
