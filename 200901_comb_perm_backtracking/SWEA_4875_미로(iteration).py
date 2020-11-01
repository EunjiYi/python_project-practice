def DFS(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    stack = []
    stack.append((r, c))
    visited.append((r, c))

    while stack:
        cr, cc = stack.pop()
        if maze[cr][cc] == "3":
            return 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != "1" and (nr, nc) not in visited:
                stack.append((nr, nc))
                visited.append((nr, nc))
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                r = i
                c = j
                break
    # 조심하자 이거 for문 안에 있어서 케이스가 새로 돌때마다 초기화되야한다.
    visited = []
    # visited를 0으로 초기화된 2차원 배열로 만들어서, 방문햇으면 visited[r][c] = 1 이런식으로 넣어도 됨

    print("#{} {}".format(tc, DFS(r, c)))