# import sys
# sys.stdin = open("input2.txt", "r")

# 전체 테스트 케이스 개수를 입력받는다.
T = int(input())
for tc in range(1, T + 1):
    ## 입력단계
    # 각각의 테스트케이스에 대해서,
    # M(가로 길이), N(세로 길이), K(연못 좌표 개수) 입력을 받는다.
    M, N, K = map(int, input().split())
    # 가로길이가 M이고 세로길이가 N인 배열 matrix를 만든다.
    matrix = [[0] * M for _ in range(N)]
    # 연못 좌표를 matrix에 넣어준다. 연못을 1로 지정한다.
    for _ in range(K):
        b, a = map(int, input().split())
        matrix[a][b] = 1

    # for row in matrix:
    #     print(*row)

    # (a, b)를 시작으로 연못을 순회하는 함수
    def dfs(r, c):
        matrix[r][c] = 0
        # 우 -> 하 -> 좌 -> 상 순서다.
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        d = 0  # 델타인덱스: dr, dc 리스트의 인덱스를 순회할 변수.

        # 순회방향이 총 4방향(우 -> 하 -> 좌 -> 상)이므로
        # 4번의 for문을 반복한다.
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 바로 인접한 곳에 연못이 있으면
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc]:
                matrix[nr][nc] = 0
                dfs(nr, nc)

    result = 0 # 연못의 갯수를 담을 변수
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:  # 연못이 있으면 순회시작.
                dfs(i, j) # (i, j)를 시작으로 연못을 순회하는 함수
                result += 1 # 한 개의 연못을 순회 완료 했으므로, 연못의 갯수를 하나 증가시킨다.

    print("#{} {}".format(tc, result))
