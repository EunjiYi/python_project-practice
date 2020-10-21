# 1954. 달팽이 숫자
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    cnt = N * N
    # delta : 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # delta = [(0,1),(1,0),(0,-1),(-1,0)]

    r = 0  # 가로좌표 0,0 부터 시작
    c = 0  # 세로좌표
    d = 0  # 델타 인덱스
    num = 1  # 증가하는 숫자( 배열에 채울 숫자)
    while num <= cnt:  # 총 N*N개의 숫자를 채워야함
        # 벽 이거나, 채울 수 없으면 방향전환
        if 0 <= r < N and 0 <= c < N and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else:  # 범위 벗어남
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
        r += dr[d]
        c += dc[d]

    for row in arr:
        print(row)

