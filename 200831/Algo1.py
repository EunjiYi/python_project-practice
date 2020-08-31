# import sys
# sys.stdin = open("input.txt", "r")

# 전체 테스트 케이스 개수를 입력받는다.
T = int(input())
for tc in range(1, T + 1):
    ## 입력단계
    # 각각의 테스트케이스에 대해서,
    # N(배열의 크기), M(첫번째 입력 값), D(변경 값) 입력을 받는다.
    N, M, D = map(int, input().split())
    # 크기가 N * N인 배열 matrix를 만든다.
    matrix = [[0] * N for _ in range(N)]

    ## 구현단계
    # 만든 배열에 중앙값(첫번째 입력값)을 넣는다.
    a = b = N //2
    matrix[a][b] = M

    # 순회를 하면서 변경값 만큼 커지거나 작아진 수들을 배열에 집어넣는다.

    # 뱡향을 전환할 델타값을 만든다.
    # 우 -> 하 -> 좌 -> 상 순서다.
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0  # 델타인덱스: dr, dc 리스트의 인덱스를 순회할 변수.

    # 순회를 시작할 초기위치를 셋팅한다.
    r = a - 1
    c = b - 1

    # 순회시작
    term = 2
    for _ in range(N//2):
        # 순회방향이 총 4방향(우 -> 하 -> 좌 -> 상)이므로
        # 4번의 for문을 반복한다.
        for _ in range(4):
            for _ in range(term):
                r = r + dr[d]
                c = c + dc[d]
                matrix[r][c] = M + D * (term//2) # 변경값을 넣어준다.
            # 한 쪽 방향이 다 완료되었으므로 방향을 바꾼다.
            d = (d + 1) % 4
        # 행과 열을 바꾸어 새로운 변경값을 넣을 초기위치로 간다.
        r = r - 1
        c = c - 1
        term = term + 2

    ## 출력단계
    #테스트 케이스 번호 출력
    print("#{}".format(tc), end = " ")
    # 각 행 별 합 출력
    for y in range(N):
        sum_value = 0
        for x in range(N):
            sum_value += matrix[y][x]
        print("{} ".format(sum_value), end = " ")
    print()