for tc in range(1, int(input())+1):

    n, E = map(int, input().split())
    #print(n, E)
    adj = [[0xfffffffff] * (n + 1) for _ in range(n + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    #print(adj)

    visit = [0]

    cost = adj[0]
    cost[0] = 0

    #print(D)
    for _ in range(n+1):
        min_c = 0xfffffff  # min cost
        min_n = -1         # min node
        # visit에 들어있지 않으면서, cost 값 중 최솟값 찾기
        for node in range(n+1):
            if node not in visit and cost[node] < min_c:
                min_c = cost[node]
                min_n = node

        # 시작노드 = 기준이 되는 노드 = min_n
        visit.append(min_n)
        # 그 노드까지 가는 최단거리 = min_c
        # min_n와 min_c모두 지금 코드라인 기분으로 다 cost에 있는 값들임.

        for nextnode in range(n+1):
            if nextnode not in visit:
                #방금 선택한 노드인 min_n를 통해서 nextnode로 가는 비용이
                #기존 cost[nextnode]로 가는 비용보다 더 싸면 업데이트
                if cost[nextnode] > min_c + adj[min_n][nextnode]:
                    cost[nextnode] = min_c + adj[min_n][nextnode]

    #print(cost)
    print("#{} {}".format(tc, cost[n]))