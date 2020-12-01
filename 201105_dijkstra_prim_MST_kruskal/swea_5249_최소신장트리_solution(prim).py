import sys
sys.stdin = open('swea_5249_최소신장트리_solution.txt')


def MST_prim():
    key = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    key[0] = 0 #key에 0 대신 1 넣어도 무방. 어떠한 점에서 시작해도 무방. 그런데 3을 넣으면 안되는 것은 일단 사용할 수 있는 정점을 넣자. tc중에 3이 없는 것도 있음.

    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        # 최소값을 가진 인덱스를 찾는다.
        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = True

        # 갱신이 가능하다면 갱신한다.
        for i in range(V + 1):
            if not visited[i] and key[i] > adj[min_idx][i]:
                key[i] = adj[min_idx][i]

    return sum(key)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        A, B, W = map(int, input().split())
        adj[A][B] = adj[B][A] = W

    print('#{} {}'.format(tc, MST_prim()))


