import heapq

'''
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

# start : 시작정점 / adj : 그래프 / weight : 시작정점으로부터 각 노드까지의 최소 비용을 저장할 배열
def dijkstra(start):
    dist = [987654321] * V
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        weight, node = heapq.heappop(heap)
        if dist[node] < weight:
            continue

        for j in range(V):
            next_weight = weight + adj[node][j]
            if dist[j] > next_weight:
                dist[j] = next_weight
                heapq.heappush(heap, (next_weight, j))

    return dist # 시작점으로부터 각 정점까지 최소비용이 저장된 배열 반환


V, E = map(int, input().split())
INF = float('inf')
adj = [[INF] * V for _ in range(V)]
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w

# 시작지점(start)으로부터 각 노드로 가는데 필요한 최소 비용을 저장하는 배열
start = 0
# weight = adj[start][:] # 초기 가중치는 인접행렬에서 시작지점 행과 같다.
result = dijkstra(start)
print(result)
