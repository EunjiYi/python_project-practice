import sys
sys.stdin = open('123.txt', 'r')

from _collections import deque

dic = {
    1 : [1, 1, 1, 1],
    2 : [1, 0, 1, 0],
    3 : [0, 1, 0, 1],
    4 : [1, 1, 0, 0],
    5 : [0, 1, 1, 0],
    6 : [0, 0, 1, 1],
    7 : [1, 0, 0, 1],
}

def condition(a, b, dir):
    next_s = matrix[a][b]
    if dir == 0: #상
        if dic[next_s][2] == 1: return True
    elif dir == 1: # 우
        if dic[next_s][3] == 1: return True
    elif dir == 2: # 하
        if dic[next_s][0] == 1: return True
    elif dir == 3: #좌
        if dic[next_s][1] == 1: return True

    return False


def check(a, b):
    x = True if 0 <= a < n and 0 <= b < m else False
    return x

# 상우하좌 순서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input())+1):

    n, m, r, c, l = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * m for _ in range(n)]


    s = matrix[r][c]
    visit[r][c] = 1
    cnt = 1

    queue = deque()
    queue.append((r, c, s, 1))


    while queue:
        cr, cc, cs, depth = queue.popleft()

        if cs == 1:
            ran = [0,1,2,3] # 상0우1하2좌3
        elif cs == 2:
            ran = [0, 2]
        elif cs == 3:
            ran = [1, 3]
        elif cs == 4:
            ran = [0, 1]
        elif cs == 5:
            ran = [1, 2]
        elif cs == 6:
            ran = [2, 3]
        elif cs == 7:
            ran = [0, 3]

        for d in ran:
            nr = cr + dr[d]
            nc = cc + dc[d]

            if check(nr, nc) == False or visit[nr][nc] == 1:
                continue
            if matrix[nr][nc] != 0 and condition(nr, nc, d) and depth < l:
                visit[nr][nc] = 1
                cnt += 1
                queue.append((nr, nc, matrix[nr][nc], depth + 1))

    print("#{} {}".format(tc, cnt))