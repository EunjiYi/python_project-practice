# 6 11
# 0 1 3
# 0 2 5
# 1 2 2
# 1 3 6
# 2 1 1
# 2 3 4
# 2 4 6
# 3 4 2
# 3 5 3
# 4 0 3
# 4 5 6
#start: 시작정점
# adj :그래프
# weight : 시작 정점으로 부터 각 노드 까지의 최소 비용을 저장할 배열
def dijkstra(start,adj,weight):
    #모든 정점을 방문할 때 까지 반복
    #1. 현재 방문하지 않은 정점중, 최소 비용으로 방문할 수 있는 정점 방문
    #2. 새로운 정점에 방문하고 나서, 그 정점으로 부터 모든 갈 수 있는 모든 정점의
    # 비용을 확인해서, 기존 최소 비용보다 더 작다면 수정.
    U = {start}   #정점을 방문할 때마다, 정점을 추가
    while len(U) < V:
        min_w = INF
        min_idx = -1
        for i in range(V):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i

        U.add(min_idx)
        for i in range(V):
            if i not in U:
                #방금 선택한 정점을 통하여 i노드로 가는 비용이
                #기존에 i로 가는 비용보다 더 싸다면, 업데이트
                tmp = min_w + adj[min_idx][i]
                if weight[i] > tmp:
                    weight[i] = tmp

    # 시작점으로 부터  각 정점 까지 최소비용이 저장된 배열 반환
    return weight

V, E = map(int,input().split())
INF = float('inf')
adj = [[INF]*V for _ in range(V)]
for i in range(E):
    s,e,w = map(int,input().split())
    adj[s][e] = w

#시작지점으로 부터 각 노드로 가는데 필요한 비용을 저장하는 배열
start = 0
weight = adj[start][:]
result = dijkstra(start,adj,weight)
print(result)


