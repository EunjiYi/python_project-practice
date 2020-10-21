
def Othello(y, x, dol):
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        Y = dy[i]
        X = dx[i]


        dol_change = []

        while True:

            if y + Y < 0 or y + Y >= N or x + X < 0 or x + X >= N or matrix[y + Y][x + X] == 0: break

            elif matrix[y + Y][x + X] == dol:

                for a, b in dol_change:
                     matrix[a][b] = dol
                break

            else:
                dol_change.append([y + Y, x + X])

            Y += dy[i]
            X += dx[i]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]


    init_pos = N // 2
    matrix[init_pos - 1][init_pos - 1] = matrix[init_pos][init_pos] = 2
    matrix[init_pos][init_pos - 1] = matrix[init_pos - 1][init_pos] = 1

    for _ in range(M):
        y, x, dol = map(int, input().split())

        matrix[y - 1][x - 1] = dol

        Othello(y - 1, x - 1, dol)


    b_cnt = w_cnt = 0
    for i in matrix:
        b_cnt += i.count(1)
        w_cnt += i.count(2)

    print('#{} {} {}'.format(tc, b_cnt, w_cnt))