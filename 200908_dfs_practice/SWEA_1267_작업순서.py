def dfs(node): # node부터 시작하여 순회하는 노드를 stack에 집어넣는 함수

    stack.append(node)
    visited[node] = 1
    checked = False


    for next_node in range(1, V+1):
        if len(check[next_node]):
            for i in range(len(check[next_node])): # 선행되어야하는 노드들이 다 선행되었으면, checked = True
                if visited[check[next_node][i]] == 0:
                    checked = False
                    break
                else:
                    checked = True
        else:
            checked = True


        if node == next_node:
            continue
        elif matrix[node][next_node] and not visited[next_node] and checked:
            dfs(next_node)

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    e_list = list(map(int, input().split()))
    matrix = [ [0] * (V+1) for _ in range(V+1)] # 간선 화살표대로 1표시
    check = [ [] * (V+1) for _ in range(V+1)] # 해당 노드보다 선행되어야하는 노드들 리스트
    for i in range(0, len(e_list), 2):
        matrix[e_list[i]][e_list[i+1]] = 1
        check[e_list[i+1]].append(e_list[i])
    #print(check)

    stack = []
    visited = [0] * (V+1)

    # 선행 노드가 제일 적은 것을 스타트로,
    min_value = float('inf')
    min_node = 0
    for i in range(1, V+1):
        if len(check[i]) < min_value:
            min_value = len(check[i])
            min_node = i
    dfs(min_node)

    while True:
        if len(stack) == V: # 다 방문했으면, 반복문 빠져나가기.
            break
        else:
            # 다 방문 안했으면, 방문 안한 노드 중에서 선행노드가 제일 적은 것을 스타트로.
            min_value = float('inf')
            min_node = 0
            for i in range(1, V + 1):
                if not visited[i] and len(check[i]) < min_value:
                    min_value = len(check[i])
                    min_node = i
            dfs(min_node)

    print(f"#{tc}", end = " ")
    for n in stack:
        print(n, end = " ")
    print()
