import sys
import heapq

sys.stdin = open('swea_5249_최소신장트리_solution.txt')


def MST_PRIM():
    visited = [False] * (V + 1) # 정점을 사용했는지 안했는지 체크

    heap = []

    # 순서중요
    # 가중치, 정점 순서 중요 - 가중치를 기준으로 먼저 순서를 매기고, 가중치가 같다면 그 다음에 작은번호 순.
    heapq.heappush(heap, (0, 0))
    ans = 0

    while heap:
        w, v = heapq.heappop(heap)  # 가중치, 정점
        if not visited[v]:
            ans += w
            visited[v] = True

            for node, weight in adj[v]:
                if not visited[node]:
                    heapq.heappush(heap, (weight, node))

    return ans


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접리스트
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        A, B, W = map(int, input().split())

        adj[A].append((B, W))
        adj[B].append((A, W))

    print('#{} {}'.format(tc, MST_PRIM()))
