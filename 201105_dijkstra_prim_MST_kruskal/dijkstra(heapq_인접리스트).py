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