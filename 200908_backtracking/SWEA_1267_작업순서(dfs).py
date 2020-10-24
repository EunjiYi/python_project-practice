#DFS
#아까전 반복문은 선행작업먼저 처리
#이번에는 깊이 우선으로 진행하면서, 후행작업먼저 stack에 넣고
#후행작업이 없으면, 자기 자신을 stack에 넣는다.
def dfs(v):
    visited[v] = 1
    #모든 후행작업 확인 후, 실행하지 않은 후행작업있으면 후행작업부터 탐색
    for i in range(1,V+1):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i)
    #for문이 끝나면, 후행작업을 모두 마친 상태
    stack.append(v)


T = 10
for tc in range(1,T+1):
    V, E = map(int,input().split())
    edges = list(map(int,input().split()))
    #각 행의 인덱스에 해당하는 노드의 후행작업 노드들 표시(인접행렬)
    adj = [[0]*(V+1) for _ in range(V+1)]
    #선행작업을 저장하는 행렬
    prev_arr = [[0]*(V+1) for _ in range(V+1)]

    stack = list() #작업순서 후행으로 먼저 push할 stack
    visited = [0]*(V+1)     #노드 방문여부 체크

    for i in range(0,len(edges),2):
        f,t = edges[i],edges[i+1]   #from/to
        adj[f][t] = 1
        prev_arr[t][f] = 1
    #선행작업이 없는 위치에서 깊이 우선탐색 실행
    for i in range(1,V+1):
        if prev_arr[i].count(1) == 0:   #선행작업 없음
            dfs(i)

    print("#{}".format(tc),*stack[::-1])