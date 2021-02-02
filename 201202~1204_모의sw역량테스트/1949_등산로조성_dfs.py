import sys
sys.stdin = open('input.txt')

def check(a, b):
    return 0 <= a < n and 0 <= b < n

def dfs(r, c):
    global result

    # visit = [[0] * n for _ in range(n)] 방문체크하면 안 됨.(주의)
    stack = [(r, c, 1)]
    # visit[r][c] = 1

    while stack:
        cr, cc, road = stack.pop()

        if result < road:
            result = road

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = cr + dr
            nc = cc + dc

            if check(nr, nc) and mount[cr][cc] > mount[nr][nc]:
                stack.append((nr, nc, road + 1))
                # visit[nr][nc] = 1


if __name__ == "__main__":
    for tc in range(1, int(input()) + 1):

        n , k = map(int, input().split())

        mount = [list(map(int, input().split())) for _ in range(n)]
        result = -float('inf')

        max_height = max(sum(mount, []))


        start = []
        for i in range(n):
            for j in range(n):
                if max_height == mount[i][j]:
                    start.append((i, j))

        for i in range(n):
            for j in range(n):
                for cut in range(k+1):
                    mount[i][j] = mount[i][j] - cut

                    for r, c in start:
                        dfs(r, c)

                    mount[i][j] = mount[i][j] + cut

        print("#{} {}".format(tc, result))
