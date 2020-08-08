T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    #map = [[0] * (N+1) for _ in range(N+1)]
    map = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * N for _ in range(N)]  # 순회했는지 기록하는 곳.
    result = [0] * 20  # 정답모음집

    # (0,0) -> (0,1) -> (0,2) -> 순서로 하나씩 탐색한다.
    # for i in range(N):
    #     for j in range(N):
    i = 2
    j = 6

    if check[i][j] == 0:
        if map[i][j] != 0:  # 탐색중에 0이 아닌 숫자발견하면 행렬시작이니까 지금부터 행렬을 찾자.
            r = i  # 가로 #행
            c = j  # 세로 #열

            # 행의 갯수 구하기
            cnt = 1
            while True:
                # check[r][c] = 1
                r = r + 1
                if r == N:
                    break
                cnt += 1
                if map[r][c] == 0:
                    # check[r][c] = 0
                    result[0] = cnt - 1
                    r = r - 1  # 하나 되돌아가기
                    break

            # 열의 갯수 구하기
            cnt = 1  # cnt초기화
            while True:
                # check[r][c] = 1
                c = c + 1
                if c == N:
                    break
                cnt += 1
                if map[r][c] == 0:
                    # check[r][c] = 0
                    result[1] = cnt - 1
                    c = c - 1  # 하나 되돌아가기
                    break

            # 카운트한 영역 다 1로 채우기
            # if r == N or c == N:
            #     r = r+1
            #     c = c+1

            for a in range(i, r-1):
                for b in range(j, c-1):
                    check[a][b] = 1



    print(result)
    for r in check:
        print(r)
    #print('#{} '.format(tc), end=" ")
    #print('#{}'.format(tc, result))