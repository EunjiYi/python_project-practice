def check(a, b):
    return 0 <= a < N and 0 <= b < N


def dfs(cr, cc, cut, ans):
    global max_ans

    if max_ans < ans:
        max_ans = ans

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = cr + dr, cc + dc

        if check(nr, nc) and visit[nr][nc] == 0:
            if mount[cr][cc] > mount[nr][nc]:
                visit[nr][nc] = 1
                dfs(nr, nc, cut, ans+1)
                visit[nr][nc] = 0

            elif cut == 0 and mount[cr][cc] > mount[nr][nc] - K:
                tmp = mount[nr][nc]
                mount[nr][nc] = mount[cr][cc] - 1 # 재귀 돌면서 한 번깎고 두 번 깎고.. K까지 깎음.
                visit[nr][nc] = 1
                #cut = 1 로 놓고 dfs(nr, nc, cut, ans+1)로 넘기니까 안됨.
                # 바로 dfs(nr, nc, 1, ans+1)로 넘기자.
                dfs(nr, nc, 1, ans+1)
                mount[nr][nc] = tmp
                visit[nr][nc] = 0



for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(N)]

    visit = [[0] * N for _ in range(N)]

    # 깎는 횟수
    cut = 0 # 안깍음
    #cut = 1이면 깎았다는 뜻.
    max_ans = 0  # 답

    # 이렇게 코드 짜면 제일 처음 만나는 최댓값에서만 시작한다. 이러면 안됨!
    # max_height = 0
    # for i in range(N):
    #     for j in range(N):
    #         if max_height < mount[i][j]:
    #             max_height = mount[i][j]
    #             max_r = i
    #             max_c = j
    # print(max_height, max_r, max_c)

    # map 전체에서 높이 최댓값 구하고 / dfs는 최댓값인 모든 지점에 대해서 따로 반복문으로 돌려야함.
    max_height = max(sum(mount, [])) # 승한이가 알려줌
    #print(max_height)

    for i in range(N):
        for j in range(N):
            # 모든 최대높이 지점에서 시작.
            if max_height == mount[i][j]:
                visit[i][j] = 1
                dfs(i, j, cut, 1)
                visit[i][j] = 0

    print("#{} {}".format(tc, max_ans))
