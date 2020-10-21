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

    connect = 0
    def DFS(s): #s노드에서 시작해서, 간선을 타고 탐색하는 함수
        global connect
        visited[s] = 1  # 얘는 참조형이라서 global 선언할 필요가 없다.
        for next in range(1, V+1):
            if matrix[s][next] and not visited[next]:
                if next == end_node:  # end node와 같다면
                    connect = 1
                    return    #return 1로 바로 안하고 connect = 1을 했다.

                DFS(next)  # 재귀함수적으로 다음 깊이로 들어간다.
    #========================함수 끝

    DFS(start_node)
    print('#{} {}'.format(tc, connect))