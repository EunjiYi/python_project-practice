for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())

    # 이거 참신하다 ㅠㅠ 반대방향 체크하는 것.
    # 또 중요한 것. 단순히 상하좌우 뿐만 아니라 이동성이 없는 0도 필요하다.
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    opposite = [0, 2, 1, 4, 3] # 반대방향

    micro = [list(map(int, input().split())) for _ in range(K)]

    def check(a, b):
        return a == 0 or a == N-1 or b == 0 or b == N-1

    for m in range(M): # 매시간마다 체크
        # 위치하는 미생물 군집 번호 적는 곳
        # 미생물이 0번부터 있어서 0도 표시하기 위해서 초기값 셋팅은 -1로
        num = [[-1] * N for _ in range(N)] # 이걸 바깥에 선언하면 안 된다. 매 시간마다 새로 리셋되어야함.

        # 2개이상(3개이상도) 합치기 위해 필요한 임시 사이즈 배열. (2개 이상)3개 이상에서 사이즈 제일 큰 거 임시저장해둠.
        size_tmp = [[0] * N for _ in range(N)]

        for k in range(K): # 각 미생물 별로 상황 체크
            dir = micro[k][3]
            if dir != 0: #상하좌우 방향성이 있다. = 즉 이동하고 있다.
                micro[k][0] = micro[k][0] + dr[dir] # 1시간 이동 후 r좌표
                micro[k][1] = micro[k][1] + dc[dir] # 1시간 이동 후 c좌표
                nr, nc = micro[k][0], micro[k][1]

                # 가장자리면
                if check(nr, nc):
                    micro[k][2] //= 2
                    if micro[k][2] > 0: #미생물이 있으면
                        micro[k][3] = opposite[dir]
                    else: # 미생물이 없으면
                        micro[k][3] = 0 #이동성 없음. ->  if dir != 0에 의해서 더 이상 체크 안함.

                # 가장자리가 아니면,
                else:
                    # 현재 이동할 자리에 아무도 없으면,
                    if num[nr][nc] == -1:
                        num[nr][nc] = k # 지금 미생물 번호입력
                        size_tmp[nr][nc] = micro[k][2]  # 지금 미생물 수 입력

                    # 이 부분 어렵다! 주의주의
                    else: # 현재 이동할 자리에 이미 다른 군집이 있으면,
                        if size_tmp[nr][nc] < micro[k][2]: # 지금 오는 군집이 기존 것보다 크기가 크면 = 지금까지 이 자리에 왔던 군집 중 가장 크기가 크면.(3개 이상도 포함)
                            size_tmp[nr][nc] = micro[k][2] # 지금 오는 군집 사이즈(현재까지 가장 큰 사이즈)를 저장
                            micro[num[nr][nc]][3] = micro[k][3] # 기존 군집의 방향을 가장 큰 군집의 방향으로. -> 이 3줄은 최대크기 군집 방향을 찾기 위한 과정.

                        # 여기에 else를 붙이지 않아서 if문을 탄 후에도 탈 수 있게 한다.
                        # 먼저 있던 군집에 합친다.
                        micro[num[nr][nc]][2] += micro[k][2] #if 문과 상관없이 사이즈는 계속 누적시킴
                        micro[k][2] = 0 # 합쳐진 군집은 사이즈를 0으로 만들기
                        micro[k][3] = 0 # 이동성도 0으로 만들기
    sum = 0
    for i in range(K):
        sum += micro[i][2]

    print("#{} {}".format(tc, sum))