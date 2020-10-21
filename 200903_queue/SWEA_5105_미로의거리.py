# import sys
# sys.stdin = open('input.txt', 'r')
def bfs():
    r = 0
    c = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                r,c = i,j
                break

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]


    visited = [[0] * N for _ in range(N)]
    queue = list()
    queue.append((r,c,0))
    while queue:

        cr,cc,length = queue.pop(0)
        visited[cr][cc] = 1

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if matrix[nr][nc] == 0:
                    queue.append((nr,nc,length+1))
                elif matrix[nr][nc] == 3:
                    return length

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(N)]
    result = bfs()
    print("#{} {}".format(tc, result))