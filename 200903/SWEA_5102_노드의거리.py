def bfs(v):
    Q = []

    #enQ
    Q.append(v)
    visit[v] = 1


    # 큐가 비어있지 않은 동안
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문을 안했다면,
        for w in range(1, V + 1):
            if G[v][w] == 1 and visit[w] == 0:
                # enQ(w), 방문처리(w)
                Q.append(w)
                visit[w] = visit[v] + 1


T = int(input())
for tc in range(1, T+1):
    # 입력 -> 인접행렬
    V, E = map(int, input().split())
    # 인접행렬초기화
    G = [[0] * (V+1) for _ in range(V+1)]
    visit = [0] * (V + 1)

    # 인접행렬 저장
    for i in range(E):
        s, e = map(int, input().split())
        G[s][e] = G[e][s] = 1

    start, end = map(int, input().split())

    bfs(start)

    if not visit[end]:
        print(f'#{tc} {visit[end]}')
    else:
        print(f'#{tc} {visit[end]-1}')