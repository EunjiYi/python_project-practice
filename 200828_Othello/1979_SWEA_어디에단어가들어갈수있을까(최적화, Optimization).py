T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        r = 0
        c = 0
        for j in range(N):
            if matrix[i][j] == 1:
                r += 1
            elif matrix[i][j] == 0:
                if r == K:
                    result += 1
                r = 0
            if matrix[j][i] == 1:
                c += 1
            elif matrix[j][i] == 0:
                if c == K:
                    result += 1
                c = 0

        if r == K:
            result += 1
        if c == K:
            result += 1

    print(f'#{tc} {result}')