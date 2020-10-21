for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    #인접리스트 이용하기
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    s, e = map(int, input().split()) #출발, 도착

    visit = [0] * (V + 1)
    Q = [s]
    visit[s] = 1    #출발점 방문하고 큐에 삽입

    while Q:    #빈큐가 아닐 동안
        v = Q.pop(0)    #큐에서 뺀다.
        for w in G[v]:
            if visit[w] == 0:
                visit[w] = visit[v] + 1 #거리계산
                Q.append(w)


    if not visit[e]:
        print(f'#{tc} {visit[e]}')
    else:
        print(f'#{tc} {visit[e]-1}')