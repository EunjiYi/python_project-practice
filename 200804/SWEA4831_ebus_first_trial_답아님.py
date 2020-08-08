T = int(input())
for tc in range(1, T+1):
    K,N,M = map(int,input().split())
    # K는 한번에 가는 거리
    # 0~N번 정류장 까지 있음
    # M은 설치된 충전기 갯수
    gas_station = list(map(int, input().split())) #충전기 장소.
    #print(K,N,M,gas_station)

    cnt = 0 #충천횟수
    run = 0 #버스가 갈 수 있는 남은 거리
    for i in range(M-1): #이걸 M이 아니고 N으로 해서 index out of range 남

        if i == 0: #첫 충전소 도착
            run = K - gas_station[0]

        if gas_station[i+1] - gas_station[i] > run: #다음충전소까지 버스가 갈 수 없으면
            cnt += 1
            run = K #갈 수 있는 거리 다시 풀충전
        else: # 다음 충전소까지 버스가 갈 수 있으면
            continue

    print(cnt)
    #print('#{} {}'.format(i, cnt))