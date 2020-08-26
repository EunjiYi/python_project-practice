"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
#인접행렬 작성하기(adjacency matrix)
adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1

visited = [0] * (N+1)
result = list()
#stack을 이용한 dfs
def dfs(v):
    stack = list()
    stack.append(v)
    visited[v] = 1  # 첫번째 노드는 stack에 추가하면서 방문
    result.append(v)
    while stack:
        current = stack[-1]
        #현재 노드에서 갈 수 있는 모든 노드 검사
        visited[current] = 1
        for i in range(len(adj[current])):
            #현재 노드와 연결되어 있고 방문하지 않은 노드라면,
            if adj[current][i] == 1 and visited[i] == 0:
                stack.append(i) # 다음방문추가
                result.append(i)
                break
        else:   # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
            stack.pop()

dfs(1)
print(result)