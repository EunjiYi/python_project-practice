
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for k in range(N-K+1):
            if sum(puzzle[i][k:k+K]) == K:
                    cnt+=1
    print(cnt)


