# 문제 미로1
import sys
sys.stdin = open("input.txt","r")


#반복구조의 dfs
def dfs():
    # 시작점 찾고,
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r,c = i,j
                break

    stack = list()
    stack.append((r,c))
    visited = [[0]*L for _ in range(L)] # 지나온 경로 표시
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    #시작점 찾으면 dfs 실행
    # while stack: # 스택이 비어있지 않으면 dfs 계속 실행
    #     #dfs 실행중 목적지 도달하면, return 1, 도달 하지 못하면 return 0
    #     cr,cc = stack[-1]   #현재노드
    #     #현재 노드에서 갈수 있는 경로 탐색
    #     #상하좌우 네방향, 미로 범위안, 벽이 아닌곳, 방문하지 않은 곳
    #     for d in range(4):
    #         nr = cr + dr[d]
    #         nc = cc + dc[d]
    #         if 0<=nr < L and 0<= nc<L and visited[nr][nc] == 0:
    #             if maze[nr][nc] == 0: #갈수 있는 경로
    #                 stack.append((nr,nc))
    #                 visited[nr][nc] = 1
    #                 break
    #             elif maze[nr][nc] == 3: # 목적지에 도달
    #                 return 1
    #     else:
    #         stack.pop()
    #########################################################################

    while stack: # 스택이 비어있지 않으면 dfs 계속 실행
        #dfs 실행중 목적지 도달하면, return 1, 도달 하지 못하면 return 0
        cr,cc = stack.pop()   #현재노드
        #현재 노드에서 갈수 있는 경로 탐색
        #상하좌우 네방향, 미로 범위안, 벽이 아닌곳, 방문하지 않은 곳
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr < L and 0<= nc<L and visited[nr][nc] == 0:
                if maze[nr][nc] == 0: #갈수 있는 경로
                    stack.append((nr,nc))
                    visited[nr][nc] = 1
                elif maze[nr][nc] == 3: # 목적지에 도달
                    return 1

    ####################################################################
    return 0


T = 10
L = 16
for t in range(T):
    tc = input()
    maze = [list(map(int,input())) for _ in range(L)]
    result = dfs()
    print("#{} {}".format(tc,result))

