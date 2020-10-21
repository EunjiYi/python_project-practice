T = int(input())
for tc in range(1,T+1):
    # K : 최대 이동가능 거리
    # M : 충전기 정류장 개수
    # N : 정류장 거리
    K, N, M = map(int,input().split())
    stations = list(map(int,input().split()))   #시작과 끝이 포함되지 않은 충전기 목록
    stations.insert(0,0)
    stations.append(N)
    pos = 0 # 자동차 위치
    cnt = 0 # 충전횟수
    # 충전기 목록 확인하면서 충전 횟수 카운팅하기
    for i in range(1,M+2): # 앞뒤로 시작과 종료지점을 추가 해서 +2
        # 현재 정류장의 위치와 이전 정류장의 위치 차가 K보다 크다면, 충전불가능
        if(stations[i] - stations[i-1]) > K : #  이동 불가능
            cnt = 0
            break
        # 충전 하려고 하는 정류장의 위치가 pos + K 보다 크다면,
        # 이전 정류장에서 충전을 해야함
        if(stations[i] > pos + K ):
            pos = stations[i-1]
            cnt += 1
    print("#%d"% tc, cnt)