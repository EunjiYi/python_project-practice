for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [[0] * (sum(score) + 1) for _ in range(N + 1)]   # 행은 높이, 열은 s

    def dfs(k, s):
        if visit[k][s]: return
        visit[k][s] = 1
        if k == N:
            return

        dfs(k + 1, s) #k번 문제를 틀렸을 때
        dfs(k + 1, s + score[k]) # k번 문제를 맞았을 때

        dfs(0,0)
        print(sum(visit[N]))