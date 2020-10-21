#DFS 연습하기~ 백준: 유기농배추
'''
0 0 0 0 0 0
0 0 0 1 1 1
0 0 0 0 1 1
0 0 1 1 1 0
0 0 0 1 1 1
0 0 0 0 1 0
'''
# arr = [[]]
arr = [list(map(int,input().split())) for _ in range(6)]
#
dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[0] * 6 for _ in range(6)]
result = 0
is_find = False
for i in range(6):
    for j in range(6):
        if arr[i][j] == 1:
            cnt = 0 #연결된 개수 세기 위한 변수
            #dfs 시작 : 반복문 > stack
            stack = list()
            stack.append((i,j))
            visited[i][j] = 1
            cnt += 1
            while stack:    # 스택에 요소가 있으면 계속 반복
                # 해당 요소에서 갈 수 있는 길을 모두 검색
                # 갈 수 있는 길이 나오면 stack에 추가, 추가했음을 표시
                cr,cc = stack[-1] #현재 노드
                # cnt += 1
                #현재 노드에서 갈 수 있는 길을 탐색
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    # nr,nc 가 범위내에있고, 한 번도 방문하지 않은 지점이면 방문
                    if 0<= nr <len(arr) and 0<= nc <len(arr) and not visited[nr][nc]:
                            if arr[nr][nc] == 1:
                                stack.append((nr,nc))
                                visited[nr][nc] =1
                                cnt += 1
                                break
                else: # 갈수 있는 길이 없음
                    stack.pop()
                    # cnt += 1
            result = cnt
            if cnt > 1:
                is_find = True
        if is_find:
            break
    if is_find:
        break


print(result)


