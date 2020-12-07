dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dfs(r, c, acc):
    global ans

    locs.append((r, c))
    foods.append(arr[r][c])


    for k in range(4):
        nr, nc = r + dr[k] , c + dc[k]
        if (nr, nc) == start_point and 0 in visit and 1 in visit and 2 in visit:
            acc += 1
            ans = max(ans, acc)
            return
        if 0 <= nr < N and 0 <= nc < N and not (nr, nc) in locs and not arr[nr][nc] in foods:
            if visit:
                if k >= max(visit):
                    visit.append(k)
                    dfs(nr, nc, acc + 1)
                    visit.pop()
                    locs.pop()
                    foods.pop()
            elif k == 0:
                visit.append(k)
                dfs(nr, nc, acc + 1)
                visit.pop()
                locs.pop()
                foods.pop()

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    for i in range(N):
        for j in range(N):
            locs = []
            foods = []
            visit = []
            start_point = (i, j)
            dfs(i, j, 0)
    print("#{} {}".format(tc, ans))