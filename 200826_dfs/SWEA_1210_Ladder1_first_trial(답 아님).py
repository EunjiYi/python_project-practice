T = 1
for tc in range(1, T+1):
    t = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    dy = {0, 1}
    dx = {1, 0}

    def dfs(y, x): #시작점이 (0, x)일 때 사다리를 타서 가장 마지막 수를 반환하는 함수
        #방문하면 0으로 만들기
        cnt = 0
        matrix[y][x] = 0
        cnt += 1

        for k in range(2):
            yy = y + dy[k]
            xx = x + dx[k]

            if matrix[yy][xx]:
                cnt += dfs(yy, xx)

        return cnt

    print(dfs(0,1))

    # index = 0
    # for i in range(100):
    #     if dfs(0, i) == 2:
    #         index = i
    #
    # print('#{} {}'.format(tc, index), end=" ")