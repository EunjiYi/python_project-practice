
def dfs(node): #node부터 시작해서 그래프를 순회하는 함수
    visited[node] = 1

    cnt = 0
    for next_node in range(1, N+1):
        if visited[next_node]:
            cnt += 1
        if cnt == N:
            return

    for next_node in range(1, N+1):
        if node == next_node:
            continue
        elif not visited[next_node] and matrix[node][next_node]:
            dfs(next_node)




if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        matrix = [[0] * (N+1) for _ in range(N+1)]

        for _ in range(M):
            a, b = map(int, input().split())
            matrix[a][b] = matrix[b][a] = 1

        visited = [0] * (N+1)

        cnt = 0
        for start in range(1, N+1):
            if not visited[start]:
                dfs(start)
                cnt += 1
        print(f'#{tc} {cnt}')