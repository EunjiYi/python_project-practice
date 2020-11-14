#현재 위치에서 움직일 수 있는 방향
dir = {1:[0,1,2,3],2:[0,1],3:[2,3],
       4:[0,3],5:[1,3],6:[1,2],7:[0,2]}
#움직이려는 방향에 어떤 모양의 통로가 있어야 움직일 수 있는 지
possible = {0:[1,2,5,6], 1:[1,2,4,7],2:[1,3,4,5],3:[1,3,6,7]}
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r,c):
    result = 1  #탈주범이 있을 수 있는 통로의 개수
    queue = list()
    queue.append((r,c,1))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    while queue:
        cr,cc,cl = queue.pop(0)
        if cl == L:
            break
        # 움직일 수 있는 위치가 정해져 있음: 현재 위치의 통로 모양에 따라서 결정
        #현재 통로의 모양 arr[cr][cc] : 1~ 7까지 중 하나
        #  : 현재 움직일 수 있는 위치
        for i in dir[arr[cr][cc]]:
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                #이동 할 건데....이동 지역에, 통로 모양에 따라서 못갈 수 도 있음
                #  i: 이동하는 방향
                # 이동하는 방향에 따라서 갈 수 있는 블럭의 모양 : possible[i]
                if arr[nr][nc] in possible[i]: # 이동가능,
                    queue.append((nr,nc,cl + 1))
                    visited[nr][nc] = 1
                    result += 1
    return result

# def dfs(r,c):
#     result = 1  #탈주범이 있을 수 있는 통로의 개수
#     queue = list()
#     queue.append((r,c,1))
#     visited = [[0] * M for _ in range(N)]
#     visited[r][c] = 1
#     while queue:
#         cr,cc,cl = queue.pop()
#         if cl == L:
#             continue
#         # 움직일 수 있는 위치가 정해져 있음: 현재 위치의 통로 모양에 따라서 결정
#         #현재 통로의 모양 arr[cr][cc] : 1~ 7까지 중 하나
#         #  : 현재 움직일 수 있는 위치
#         for i in dir[arr[cr][cc]]:
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
#                 #이동 할 건데....이동 지역에, 통로 모양에 따라서 못갈 수 도 있음
#                 #  i: 이동하는 방향
#                 # 이동하는 방향에 따라서 갈 수 있는 블럭의 모양 : possible[i]
#                 if arr[nr][nc] in possible[i]: # 이동가능,
#                     queue.append((nr,nc,cl + 1))
#                     visited[nr][nc] = 1
#                     result += 1
#     return result


T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = dfs(R,C)
    print("#{} {}".format(tc,result))








