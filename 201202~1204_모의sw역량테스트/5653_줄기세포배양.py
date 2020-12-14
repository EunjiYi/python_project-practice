dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def f(N, M, K, org):
    d = K//2
    ts = [[-1] * (M + K) for _ in range(N+K)] #time stamp
    cell = [[0] * (M+K) for _ in range(N+K)] #줄기세포
    for i in range(N):
        for j in range(M):
            cell[i+d][j+d] = org[i][j] #중간으로 옮김
            if org[i][j] != 0: #초기에 세포가 있으면 timestamp 0으로
                ts[i+d][j+d] = 0

    for h in range(1, K+1): #배양시간별 각 칸의 상태 정의
        for i in range(d-h//2, N+d+h//2): #시간이 지날수록 확인 영역 확장 -> 생명력이 1이어도 2시간에 한 번씩 번식하니까 h//2
            for j in range(d-h//2, M+d+h//2):
                tmp = [] #주변의 활성세포 생명력 테스트
                if cell[i][j] == 0: #아직 세포가 없으면
                    for k in range(4): #주변 확인
                        ni = i + dr[k]
                        nj = j + dc[k]
                        if 0 <= ni < N + K and 0 <= nj < M+K: # 사실 초기 배열차제를 크게 줬기 때문에 필요하진 않음
                            if cell[ni][nj] > 0 and ((h-ts[ni][nj])/cell[ni][nj]) > 1: # 활성세포가 있으면
                                tmp.append(cell[ni][nj]) #생명력 리스트 만듦
                        if len(tmp) > 0:
                            cell[i][j] = max(tmp) #세포생성
                            ts[i][j] = h #세포 생성 시간 기록
    cnt = 0
    for i in range(N + K):
        for j in range(M + K):
            if cell[i][j] > 0 and (K-ts[i][j])//cell[i][j]<2:
                cnt += 1
    return cnt



for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, K, org)
    print("#{} {}".format(tc, r))

