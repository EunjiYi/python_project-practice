T = 10
for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [0] * (sum(score) + 1)
    Q = [0]

    # 너비우선탐색인데, 큐에 넣고 빼는 번거로운 작업을 없앤 것.
    for val in score:
        for i in range(len(Q)):
            if visit[ Q[i] + val ]: continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)
