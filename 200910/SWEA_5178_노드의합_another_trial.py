for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    T = [0] * (N + 1)
    for _ in range(M):
        num, val = map(int, input().split())
        T[num] = val

    # 채워져있는 부분말고 안채워진 제일 밑 노드부터 올라오자.
    for i in range(N - M, 0, -1): #배열의 인덱스이자 노드의번호
        T[i] = T[i * 2]
        if i * 2 + 1 <= N: # 가장 마지막에 오른쪽 자식이 없을 수 있으니까 반드시 있는지 체크부터하고 더해야함. 아니면 인텍스 오류난다.
            T[i] += T[i * 2 + 1]
    print(T[L])


    # 고전
    # def dfs(v):
    #     if v > N: return 0
    #     l = dfs(v * 2)
    #     r = dfs(v * 2 + 1)
    #     T[v] += l + r
    #     return T[v]
    #
    #
    # dfs(1)
    # print(T[L])

