for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score) + 1) #마지막에 중복을 제거

    def dfs(k, s):
        if k == N:
            visit[s] = 1 #방문체크 
        else:
            dfs(k + 1, s) #k번 문제를 틀렸을 때
            dfs(k + 1, s + score[k]) # k번 문제를 맞았을 때

        dfs(0,0)
        print(sum(visit))