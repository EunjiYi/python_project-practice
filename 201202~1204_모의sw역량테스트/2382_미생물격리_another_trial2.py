

class B:
    def __init__(self, x, y, cnt, dir):
        self.x, self.y, self.cnt, self.dir = x, y, cnt, dir


deltas = (tuple(), (-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    T = int(input())

    for t in range(1, T + 1):
        N, M, K = map(int, input().split())

        cells = [[None] * N for _ in range(N)]
        bs = {B(*map(int, input().split())) for _ in range(K)}

        for m in range(M):
            d = {}
            for b in bs:
                dx, dy = deltas[b.dir]

                b.x += dx
                b.y += dy
                d.setdefault((b.x, b.y), []).append(b)

                if b.x == 0 or b.x == N - 1 or b.y == 0 or b.y == N - 1:
                    b.cnt //= 2
                    if b.dir == 1:
                        b.dir = 2
                    elif b.dir == 2:
                        b.dir = 1
                    elif b.dir == 3:
                        b.dir = 4
                    elif b.dir == 4:
                        b.dir = 3

            for (x, y), b_list in d.items():
                if len(b_list) <= 1:
                    continue

                new_b = B(x, y, sum(map(lambda b: b.cnt, b_list)), max(b_list, key=lambda b: b.cnt).dir)
                bs.add(new_b)
                bs.difference_update(b_list)

        ans = sum(map(lambda b: b.cnt, bs))

        print(f'#{t} {ans}')


if __name__ == '__main__':
    solve()