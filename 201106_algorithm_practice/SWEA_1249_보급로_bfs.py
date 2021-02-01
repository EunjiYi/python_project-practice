from _collections import deque


def check(a, b):
    x = True if 0 <= a < n and 0 <= b < n else False
    return x


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    # print(matrix)
    cost = [[0xffffffff] * n for _ in range(n)]
    # print(cost)

    cost[0][0] = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        cr, cc = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = cr + dr
            nc = cc + dc

            if check(nr, nc) and cost[nr][nc] > cost[cr][cc] + matrix[nr][nc]:
                cost[nr][nc] = cost[cr][cc] + matrix[nr][nc]
                queue.append([nr, nc])

    print("#{} {}".format(tc, cost[n - 1][n - 1]))