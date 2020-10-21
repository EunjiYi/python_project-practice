for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score) + 1)
    Q = [[0, 0]] # k, s
    while Q:
        k, s = Q.pop(0)
        if k == N:
            visit[s] = 1
        else:
            Q.append([k + 1, s])
            Q.append([k + 1, s + score[k]])
            
    print(sum(visit))