def dfs(n):
    stack = list()
    stack.append(n)
    visited[n] = 1
    while stack:
        cur = stack[-1]
        #현재 노드에서 연결된 모든 사람 찾기
        # is_find = False
        for i in range(1,N+1):
            #현재 사람과 연결되어있고, 방문하지 않았다면 방문
            if adj[cur][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = 1
                # is_find = True
                break
        else:
            stack.pop()  # 현재노드 stack에서 삭제
        # if not is_find:
        #     stack.pop() #현재노드 stack에서 삭제


T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    visited = [0]*(N+1)
    result = 0
    for i in range(1,N+1):
        # i번 사람부터 시작해서 연결되는 모든 무리를 순회
        #dfs,bfs
        if not visited[i]:
            dfs(i)
            result += 1
    print("#{} {}".format(tc,result))