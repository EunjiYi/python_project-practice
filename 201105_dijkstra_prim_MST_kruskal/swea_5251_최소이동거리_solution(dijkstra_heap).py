import sys
import heapq
sys.stdin = open('swea_5251_최소이동거리_solution.txt')

def dijkstra_heap():
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    heap = []
    dist[0] = 0
    heapq.heappush(heap, (0, 0)) # 순서조심. 가중치, 정점 순

    while heap:
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w

            for i in range(V + 1):
                if not visited[i] and dist[i] > dist[v] + adj[v][i]: # dist[i] > dist[v] + adj[v][i] 이부분은 안 넣어도됨. 어차피 최소힙이고 방문체크를 하니까. 그러나 이것을 넣으므로서 우리가 갱신할 수 있는 값이면 힙에 넣어버리니까 조금이라도 빠른 연산 가능.
                    heapq.heappush(heap, (dist[v] + adj[v][i], i))

    return dist[V]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        st, ed, w = map(int, input().split())

        adj[st][ed] = w

    print('#{} {}'.format(tc, dijkstra_heap()))