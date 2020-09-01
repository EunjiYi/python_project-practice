### DFS 알고리즘 - 반복문으로 짜기
# 수도코드
# STACK s
# visited[]
# DFS(v)
#     push(s, v)
#     WHILE NOT isEmpty(s)
#         v <- pop(s)
#         IF NOT visited[v]
#             visit(v)
#             FOR each w in adjacency(v)
#                 IF NOT visited[w]
#                     push(s, w)

### cf. DFS알고리즘 - 재귀로 짜기
# 수도코드
# DFS_Recursive(G, v)
#   visited[v] <- TRUE  // v 방문 설정
#   FOR each all w in adjacency(G, v)
#       IF visited[w] != TRUE
#           DFS_Recursive(G, w)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # V
    matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬(노드가 1부터 있으니까 V+1)
    visited = [0] * (V + 1)  # 인덱스 1부터 쓰려고

    for i in range(E):  # 간선의 갯수만큼 돌리기
        start, end = map(int, input().split())
        matrix[start][end] = 1  # 간선이 연결되어 있으면 1로 바꾼다.

    # 정답 찾을 출발/도착노드
    start_node, end_node = map(int, input().split())
    # =================여기까지가 입력받기


    result = list() # 순회하는 순서를 찍어주는 result
    #이 문제에서는 필요없지만 연습삼아 적어봤다.

    connect = 0
    stack = list()

    #stack을 이용한 dfs
    def dfs(v):
        global connect

        stack.append(v)
        visited[v] = 1  # 첫번째 노드는 stack에 추가하면서 방문
        result.append(v)

        while stack:
            current = stack[-1]
            #현재 노드에서 갈 수 있는 모든 노드 검사
            visited[current] = 1
            for i in range(len(matrix[current])):
                #현재 노드와 연결되어 있고 방문하지 않은 노드라면,
                if matrix[current][i] == 1 and visited[i] == 0:
                    if i == end_node:  # end node와 같다면
                        connect = 1
                        return  # return 1로 바로 안하고 connect = 1을 했다.

                    stack.append(i) # 다음방문추가
                    result.append(i)
                    break
            else:   # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
                stack.pop()

    dfs(start_node)
    #print(result)
    print('#{} {}'.format(tc, connect))

