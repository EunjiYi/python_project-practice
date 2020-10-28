### DFS

```python
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if maze[nr][nc] == 3:
            return 1
        if 0<= nr <L and 0<=nc <L and not visited[nr][nc] and not maze[nr][nc]:
            if dfs(nr,nc):  #다음 단계에서 경로를 찾았으면, 다른 경로는 찾을 필요없음
                return 1
    return 0
```



```python
def dfs(r,c):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visited = [[0] * L for _ in range(L)]
    stack = list()
    stack.append((r,c))

    while stack: # 스택이 비어있지 않다면 계속반복
        cr,cc = stack[-1]
        visited[cr][cc] = 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            #범위내에 있고, 방문안했고, 통로여야 됨
            if 0<= nr < L and 0<= nc < L and not visited[nr][nc] and maze[nr][nc] ==0:
                stack.append((nr,nc))
                break
            elif maze[nr][nc] == 3:
                return 1
        else:   # for문에서 break가 안걸렸다면, 길이 없음.
            #현재노드(stack의 top) 더 이상 검사할 필요없음
            stack.pop()
    return 0
```



`+`

이거랑 구분하기(시뮬레이션)

```python
N = 10
#보드에 놓인 퀸이 영향을 미치는 곳을 표시하기 위한 배열
check = [[0] * N for _ in range(N)]
cnt = 0
def marking(r,c,num):
    # r,c에 놓여진 퀸에 의해 영향받는 칸에 num을 더해주는 함수
    # num은 1 또는 -1
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 > nr or 0 > nc or nr >= N or nc >= N:
                break
            check[nr][nc] += num
```





### BFS

```python
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
result = 0 # 정답

def bfs(r, c, height):
    global result
    visited[r][c] = 1
    Q = []
    Q.append((r, c))
    count = 1 # height 높이일 때 채워야할 물 갯수
    isSide = False
    while Q:
        cr, cc = Q.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 수영장 경계체크/가장자리 체크가 너무 어려웠다 ㅠㅠ
            if not (0 <= nr < N and 0 <= nc < M):
                isSide = True
                continue

            # 아예 한 번에 경계값 빼버렸는데 이러면 제대로 안나옴
            #if 0 < nr < N - 1 and 0 < nc < M - 1 and pool[nr][nc] <= height and not visited[nr][nc]:

            # 선택한 높이(height)보다 낮거나 같다면 이동가능
            if pool[nr][nc] <= height and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                count += 1
    if not isSide:
        result += count
```

