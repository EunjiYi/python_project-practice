from _collections import deque

for tc in range(1, int(input())+1):

    n, E = map(int, input().split())
    #print(n, E)
    adj = [[] for _ in range(n + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    cost = [0xfffffffff] * (n+1)
    cost[0] = 0

    queue = deque()
    queue.append(0) # 0정점번호 / cost = 0

    while queue:
        c_node = queue.popleft()
        for e, w in adj[c_node]:
            if cost[e] > cost[c_node] + w:
                cost[e] = cost[c_node] + w
                queue.append(e)

    print("#{} {}".format(tc, cost[n]))