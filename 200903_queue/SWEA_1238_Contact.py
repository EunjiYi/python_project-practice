# start부터 순회를 시작하여 마지막으로 연락받는 노드 중 최댓값을 출력하는 함수
def bfs(start):
    queue = list()
    # 현재노드, 시작점으로부터 떨어진 거리를 큐에 넣는다.
    queue.append((start,0))
    #visited[start] = 1 # 사실 없어도됨.
    #가장 먼 거리, 가장 큰 노드 숫자
    mcnt = 0
    mnum = 0

    while queue:
        current, cnt = queue.pop(0)
        # 가장 큰 cnt = 가장 먼 거리 추출
        if cnt > mcnt:
            mcnt = cnt
            mnum = current
        # 먼 거리가 같다면 그 중에 가장 큰 노드 추출
        elif cnt == mcnt and current > mnum:
            mnum = current

        for node in range(N):
            # 해당 노드(node)가 지금 노드(current)와 연결되어있고, 방문하지 않았으면
            if adj[current][node] and not visited[node]:
                queue.append((node, cnt + 1))
                visited[node] = 1 # visited조심. 위치에 따라 답이 달라질 수 있다.

    return mnum

#테스트 케이스 갯수
T = 10
# 1부터 사용할거라 101까지.
N = 101
for tc in range(1, T+1):
    # 데이터길이와 시작노드를 받는다.
    length, start = map(int,input().split())
    # 인접리스트 생성
    adj = [[0] * N for _ in range(N)]
    # 노드끼리 연결되어있는 정보 받기
    node = list(map(int,input().split()))
    # 방문할 노드를 체크할 리스트
    visited = [0] * N

    for i in range(0, length, 2):
        adj[node[i]][node[i+1]] = 1

    result = bfs(start)

    print("#{} {}".format(tc, result))