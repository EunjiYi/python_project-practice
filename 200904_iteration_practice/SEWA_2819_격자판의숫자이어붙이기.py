def dfs(r, c, cnt, numbers):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    d = 0
    numbers += matrix[r][c]
    if cnt == 7:
        result.append(numbers)
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, cnt+1, numbers)




T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, '')
    fin = set(result)
    print('#{} {}'.format(tc, len(fin)))


