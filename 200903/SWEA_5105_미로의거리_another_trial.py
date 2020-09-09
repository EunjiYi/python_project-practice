dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [input() for _ in range(N)] #문자열로 받고 싶을 때
    #maze = [list(map(int, input())) for _ in range(N)] # 정수형으로 받고 싶을 때

    sx = sy = ex = ey = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            elif maze[i][j] == '3':
                ex, ey = i, j

    visit = [[0] * N for _ in range(N)]
    Q = [[sx, sy]]
    visit[sx][sy] = 1

    while Q:
        x, y = Q.pop(0)

        # 중간에 목표지점 도착해서 끊고 싶으면 (여기 아니면)
        if x == ex and y == ey:
            break

        for i in range(4):
            tx, ty =  x + dx[i], y + dy[i]
            # 경계체크, 갈수있는지 체크, 방문했는지 체크 = 3가지 순서대로 체크하기
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if maze[tx][ty] == '1' or visit[tx][ty]: continue

            visit[tx][ty] = visit[x][y] + 1

            # 중간에 목표지점 도착해서 끊고 싶으면 (여기에 넣으면 됨. )
            # 일단은 문제에서 요구하는것부터 잘 짜고, 결과 나오고 나서 끊는 것 구현하자. 조금씩 확장시키기 한 번에 잘하려고 ㄴㄴ
            # if tx == ex and ty == ey:
            #     Q.clear(); break

            Q.append([tx, ty])

    if visit[ex][ey]: visit[ex][ey] -= 2 # 도착하는 경우에 출발점, 도착점 두 개 빼야되서 -2
    print(f'#{tc} {visit[ex][ey]}') # 도착하지 못하는 경우는 그냥 0 출력