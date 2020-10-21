for tc in range(1, 11):
    N, s = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[0] * 101 for _ in range(101)] #정점번호 1~100
    for i in range(0, N, 2):        # arr[i] --> arr[i+1]
        G[arr[i]][arr[i+1]] = 1

    visit = [0] * 101
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, 101):
            if G[v][w] and not visit[w]:
                visit[w] = visit[v]+1
                Q.append(w)

    ans = 1
    for i in range(2, 101):
        if visit[ans] <= visit[i]:
            ans = i
    print(f'#{tc} {ans}')