import sys
sys.stdin = open("sample_input.txt", "r")

def DFS(a): # 갈 수 있으면 1, 갈 수 없으면 0을 반환하는 함수
    visited[a] = 1
    if a == e:
        return 1
    for w in range(1, V + 1):
        if G[a][w] == 1 and visited[w] == 0:
            if DFS(w):
                return 1
    return 0

for rc in range(1, int(input()) + 1):
    V, E =  map(int, input().split())
    # 인접 행렬 G
    # 정점 번호 1 ~ V
    G = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E): #간선 정보 읽기
        u, v = map(int, input().split())
        G[u][v] = 1

    s, e = map(int, input().split())
    visited = [0] * (V + 1)

    print(DFS(s))
