dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(y, x):
    global result
    visited.append((y, x))

    if Map[y][x] == 3:
       result = 1
       return

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and ( Map[ny][nx] == 0 or Map[ny][nx] == 3 ) and (ny, nx) not in visited:
            DFS(ny, nx)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                y, x = i, j

    # 조심하자 이거 for문 안에 있어서 케이스가 새로 돌때마다 초기화되야한다.
    visited = []
    result = 0

    DFS(y, x) # y, x를 시작으로 미로를 찾는 함수
    print('#{} {}'.format(tc, result))



