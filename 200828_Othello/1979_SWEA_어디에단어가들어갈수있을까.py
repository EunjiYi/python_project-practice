T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt = 0
        j = 0
        while True:
            if matrix[i][j]:
                cnt += 1
                j += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
                j += 1

            if j == N:
                if cnt == K:
                    result += 1
                break


    for j in range(N):
        cnt = 0
        i = 0
        while True:
            if matrix[i][j]:
                cnt += 1
                i += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
                i += 1
            if i == N:
                if cnt == K:
                    result += 1
                break

    print("#{} {}".format(tc, result))