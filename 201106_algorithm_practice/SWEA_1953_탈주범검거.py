import sys
sys.stdin = open('123.txt', 'r')

from _collections import deque

dic = {  # 상우하좌 순서
    1: [1, 1, 1, 1],
    2: [1, 0, 1, 0],
    3: [0, 1, 0, 1],
    4: [1, 1, 0, 0],
    5: [0, 1, 1, 0],
    6: [0, 0, 1, 1],
    7: [1, 0, 0, 1],
}


# 현재위치에서 (a, b)로, dir 방향으로 갈 수있는지 체크하는 함수
def condition(a, b, dir):
    # cur_s = matrix[c][d] # 지금 모양
    next_s = matrix[a][b]  # 다음 단계 모양
    if dir == 0:  # 상
        if dic[next_s][2] == 1: return True  # 하
    elif dir == 1:  # 우
        if dic[next_s][3] == 1: return True  # 좌
    elif dir == 2:  # 하
        if dic[next_s][0] == 1: return True  # 상
    elif dir == 3:  # 좌
        if dic[next_s][1] == 1: return True  # 우

    return False


# 경계값 체크하는 함수
def check(a, b):
    x = True if 0 <= a < n and 0 <= b < m else False
    return x


# 상우하좌 순서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input()) + 1):

    n, m, r, c, l = map(int, input().split())
    # print(n, m, r, c, l)
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # print(matrix)

    # 방문체크
    visit = [[0] * m for _ in range(n)]

    # 초기값 세팅
    s = matrix[r][c]
    visit[r][c] = 1
    cnt = 1

    queue = deque()
    queue.append((r, c, s, 1))  # 시작점좌표와 시작점의 모양 s= shape #depth = l까지 돌아야함.

    while queue:
        cr, cc, cs, depth = queue.popleft()  # cs = 현재 모양 / d = 현재 depth

        if cs == 1:
            ran = [0, 1, 2, 3]  # 상0우1하2좌3
        elif cs == 2:
            ran = [0, 2]  # 상하
        elif cs == 3:
            ran = [1, 3]  # 우좌
        elif cs == 4:
            ran = [0, 1]  # 상우
        elif cs == 5:
            ran = [1, 2]  # 우하
        elif cs == 6:
            ran = [2, 3]  # 하좌
        elif cs == 7:
            ran = [0, 3]  # 상좌

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