# 문제 미로1
import sys
sys.stdin = open("input.txt","r")

dr = [-1,1,0,0]
dc = [0,0,-1,1]
#반복구조의 dfs
def dfs(r,c):
    visited[r][c] = 1
    # 갈 수 있는 모든 경로에 대해서 탐색
    # 갈 수 있는 길이 있으면, 다음 노드 탐색
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
            if maze[nr][nc] == 0:
                if dfs(nr,nc) == 1:
                    return 1
            elif maze[nr][nc] == 3: # 목적지 찾음
                return 1

    return 0


T = 10
L = 16
for t in range(T):
    tc = input()
    maze = [list(map(int,input())) for _ in range(L)]
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                  r,c = i,j

    visited = [[0] * L for _ in range(L)]
    result = dfs(r,c)
    print("#{} {}".format(tc,result))

