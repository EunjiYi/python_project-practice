T = int(input())
for tc in range(1, T+1):
    K,N,M = map(int,input().split())
    gas_station = list(map(int, input().split())) #충전소
    station = [0] * (N+1) #정류장

    for i in range(len(gas_station)):
        station[gas_station[i]] += 1  #충전소가 있는 정류장에 1표시

    start = 0
    end = K
    result = 0

    while True:
        fill = 0
        for i in range(start+1, end+1):
            if station[i]: #현재 버스 위치에 충전소가 있으면,
                start = i
            else:
                fill += 1
        if fill >= K:
            result = 0
            break

        result += 1
        end = start + K
        if end >= N:
            break

    print(f'#{tc} {result}')



