다익스트라 구현

```python
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
def dijkstra(start, adj, weight):
    U = {start} # 정점을 방문할때마다 정점을 추가

    # 모든 정점을 방문할 때까지 반복
    while len(U) < V: # U에 모든 정점이 추가되면 while문 종료
        # 1. 현재 방문하지 않은 정점 중, 최소 비용으로 방문할 수 있는 정점 방문
        min_w = INF
        min_idx = -1
        for i in range(V):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i
        U.add(min_idx)

        # 2. 그 정점으로부터 갈 수 있는 방문하지 않은 모든 정점의 비용을 확인해서 최소 비용으로 갱신
        for j in range(V):
            if j not in U:
                tmp = min_w + adj[min_idx][j]  # 좀 전에 방문한 정점을 통하여 j노드로 가는 비용
                # tmp가 기존에 j로 가는 비용보다 작으면 갱신
                if weight[j] > tmp:
                    weight[j] = tmp

    return weight # 시작점으로부터 각 정점까지 최소비용이 저장된 배열 반환


V, E = map(int, input().split())
INF = float('inf')
adj = [[INF] * V for _ in range(V)]
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w

# 시작지점(start)으로부터 각 노드로 가는데 필요한 최소 비용을 저장하는 배열
start = 0
weight = adj[start][:] # 초기 가중치는 인접행렬에서 시작지점 행과 같다.
result = dijkstra(start, adj, weight)
print(result)

```



다익스트라 - heapq 사용(인접리스트)

```python
import heapq

def dijkstra(start):
    dist = [987987987987987987987] * v
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        weight, node = heapq.heappop(heap)
        if dist[node] < weight:
            continue

        for w, j in adj[node]:
            next_weight = weight + w
            if dist[j] > next_weight:
                dist[j] = next_weight
                heapq.heappush(heap, (next_weight, j))
    return dist

v, E = map(int, input().split())
inf = float('inf')
adj = [[] for _ in range(v)]

for i in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

start = 0
result = dijkstra(start)
print(result)
```





다익스트라 - heapq 사용(인접행렬)

```python
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

```





실제 문제 풀이 - 프로그래머스 합승택시요금

```python
import heapq

def solution(n, s, a, b, fares):

    link = [[] for _ in range(n+1)]
    for x, y, z in fares:
        link[x].append((z, y))
        link[y].append((z, x))

    def dijkstra(start):
        dist = [987654321] * (n + 1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # print(dp)
    answer = 987654321
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer
```

