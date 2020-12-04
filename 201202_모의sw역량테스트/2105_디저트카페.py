def check(a, b):
    return 0 <= a < N and 0 <= b < N

dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

def dfs(r, c): # r, c에서 시작해서 최대로 먹을 수 있는 디저트 갯수를 카운트 하는 함수
    ate = []
    visit = [[False] * N for _ in range(N)]
    stack = [(r, c, 1)]
    flag = False
    d_check = [0, 0, 0, 0]
    cir_cnt = 1
    while stack:
        cr, cc, cnt = stack.pop()
        if flag and cr == r and cc == c: # 가장 처음에 if문 들어가지 않도록 flag 설정
            break
        flag = True
        ate.append(matrix[cr][cc])
        #for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for d in range(4):
            d == 1:
                 d = 1 or d =

            d == 2

            d == 3

            d == 4

            nr, nc = cr + dr[d], cc + dc[d]
            if check(nr, nc) and visit[nr][nc] == False and matrix[nr][nc] not in ate:
                visit[nr][nc] = True
                stack.append((nr, nc, cnt + 1))

    result2 = [1]
    if cr == r and cc == c:
        result2.append(cnt)
    return max(result2)

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            result.append(dfs(i, j)) # result = i. j에서 출발했을 때 먹을 수 있는 디저트 최대 갯수

    print(result)

    ans = max(result)
    if ans == 1:
        ans = -1
    print("#{} {}".format(tc, ans))
