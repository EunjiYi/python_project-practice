#신나는 DFS 시간
"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,input().split()))
#인접행렬 작성하기(adjacency matrix)
adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1

# for row in adj:
#     print(row)

#방문검사 배열이 필요 : visited >> 노드의 길이 + 1
visited = [0] * (N+1)
result = list()
def dfs(v):
    global result
    if visited[v]: # 이미 방문한 노드라면 종료
        return
    #방문하지 않는 노드: 나랑 연결되어 있는 모든 노드들을 순회
    result.append(v)    #방문을 했으니 방문 순서에 추가
    visited[v] = 1  # 방문한 노드임을 표시
    #다음 노드들을 검색
    for i in range(len(adj[v])):
        if adj[v][i] == 1:  # [0,0,0,0,1,1,0,0]
            dfs(i)

dfs(1)
print(result)


