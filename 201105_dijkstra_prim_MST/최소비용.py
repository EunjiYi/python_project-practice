from _collections import deque

def check(a, b):
    x = True if 0 <= a < n and 0 <= b < n else False
    return x

for tc in range(1, int(input())+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    #print(matrix)

    cost = [[0xffffffffff] * n for _ in range(n)]
    cost[0][0] = 0 # 초기값 셋팅

    queue = deque()
    queue.append((0,0)) # r, c

    while queue:
        cr, cc = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc =  cr + dr, cc + dc

            tmp = 0
            if check(nr, nc) and matrix[nr][nc] > matrix[cr][cc]:
                tmp = matrix[nr][nc]-matrix[cr][cc]

            if check(nr, nc) and cost[nr][nc] > cost[cr][cc] + 1 + tmp:
                cost[nr][nc] = cost[cr][cc] + 1 + tmp
                queue.append((nr, nc))

    print("#{} {}".format(tc, cost[n-1][n-1]))