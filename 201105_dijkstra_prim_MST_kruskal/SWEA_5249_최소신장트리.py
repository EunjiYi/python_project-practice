for tc in range(1, int(input())+1):

    n, E = map(int, input().split())
    #print(n, E)
    adj = [[] for _ in range(n + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
        adj[e].append([s, w])

    INF = float('inf')
    cost = [INF] * (n+1)
    cost[0] = 0

    visit = [] # 방문체크, 다 돌고 나면 순회순서를 알 수 있으나 의미 없다.
    #그냥 전체 다 만들어놓고 방문했으면 1로 바꾸는게 날듯.
    #주의사항: 여기에 visit=[0]이렇게 0을 넣고 시작하면 안된다. min_n으로 0을 찾아서 visit.append(0)이 되어야함
    #안그러면 전혀 돌지 않음.

    # 최소신장트리니까 각 노드의 부모를 저장한다.
    # 이 문제에서 정답과는 상관없으나 최소신장트리를 만드는데 필요하다.
    parents = [0] * (n+1)

    # 최소신장트리 가중치 다 더한 정답
    result = 0

    for _ in range(n+1):
        min_c = INF
        min_n = -1
        for node in range(n+1):
            if node not in visit and cost[node] < min_c:
                min_c = cost[node]
                min_n = node

        # 방문한적 없으면서 현재 cost가 최소인 노드 = min_n
        visit.append(min_n)
        # 선택되었으니 가중치 더하기
        result += min_c

        for e, w in adj[min_n]:
            if e not in visit and cost[e] > w:
                cost[e] = w #min_n노드로부터 e노드로 가는 최소비용
                parents[e] = min_n

    print("#{} {}".format(tc, result))