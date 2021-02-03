from _collections import deque

for tc in range(1, 11):
    n, start_node = map(int, input().split())
    contact = list(map(int, input().split()))

    adj = [[] for _ in range(101)]
    for i in range(0, n, 2):
        adj[contact[i]].append(contact[i+1])

    visit = [0] * 101
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        for next_node in adj[node]:
            if visit[next_node] == 0:
                visit[next_node] = visit[node] + 1
                queue.append(next_node)

    ans = 1
    for i in range(2, 101):
        if visit[ans] <= visit[i]:
            ans = i

    print("#{} {}".format(tc, ans))