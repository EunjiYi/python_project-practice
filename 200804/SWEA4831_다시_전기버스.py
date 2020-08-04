T = int(input())
for tc in range(1, T+1):
    K,N,M = map(int,input().split())
    # K는 한번에 가는 거리
    # 0~N번 정류장 까지 있음
    # M은 설치된 충전기 갯수
    gas_station = list(map(int, input().split())) #충전기 장소.
    #print(K,N,M,gas_station)

    #충전소 간격이 K보다 큰 것이 하나라도 있으면 False찍고 끝내기, 즉 버스가 종점까지 절대 못김
    bool = True
    for i in range(M-1):
        if gas_station[i] - gas_station[i-1] > K:
            bool = False
            print('#{} 0'.format(tc))
            break

    cnt = 0
    bus_position = 0 #지금 버스가 있는 지점
    while bool: #충전소 간격이 K보다 큰 것이 하나도 없음 = 즉, 버스가 종점까지 갈 수 있음
        bus_position = bus_position + K  #출발점 0에서 K만큼 간다(=최대로 간다)

        # 이 과정을 종점에 도착할 때까지 반복
        if bus_position >= N-K: # 버스가 N-K까지 도착할 수 있으면 종점인 N은 당연히 도착할 수 있으니까. = 이거 한번간거 +1해야되서 최종cnt+1임
            print('#{} {}'.format(tc, cnt+1))
            break

        # 종점이 아닐 경우
        else:
            #이렇게 했더니 100점
            for n in range(K):
                if bus_position - n in gas_station:
                    cnt += 1
                    bus_position = bus_position - n
                    break
            #이렇게 했더니 70점
            # if not bus_position in gas_station: #지금 버스가 있는 지점에 충전소가 없으면
            #     bus_position = bus_position -1  #충전소가 없어서 한 번 뒤로 갔음. 근데 거기에도 충전소가 없으면? 또 하나더 뒤로 가야되는데 여기서는 bus_position = bus_position + K를 타버림. 즉, 충전도 안했는데 출발~ ㅠㅠㅠㅋㅋ
            # if bus_position in gas_station: #지금 버스가 있는 지점에 충전소가 있다면
            #     cnt += 1

         
