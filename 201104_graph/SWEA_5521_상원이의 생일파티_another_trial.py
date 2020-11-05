import sys
sys.stdin = open('상원이의 생일파티.txt')

def bfs(v):
    global cnt
    Q = list()
    Q.append((v, 0))
    visit[v] = 1
    while Q:
        cv, dis = Q.pop(0)
        for bf in G[cv]:
            if not visit[bf] and dis <= 1:
                Q.append((bf, dis + 1))
                visit[bf] = 1
                cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    # print(G)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # print(G)
    # 친구의 수
    cnt = 0
    visit = [0] * (N + 1)
    bfs(1)
    print("#{} {}".format(tc, cnt))
