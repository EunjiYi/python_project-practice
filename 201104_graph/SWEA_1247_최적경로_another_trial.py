T  = int(input())
for tc in range(1,T+1):
    N = int(input())
    loc = list(map(int,input().split()))
    comp = (loc[0],loc[1])  # 회사 좌표
    home = (loc[2],loc[3])  # 집좌표
    cust = list()
    for i in range(4,len(loc),2):
        cust.append((loc[i],loc[i+1]))

    #고객 방문 순서 바꿔가며 모든 경우의 수 체크 : 순열
    visited = [0] * N
    min_dist = 0xffffffffff
    def solve(idx,dist,x,y):
        global min_dist
        if dist > min_dist:
            return
        if idx == N:
            # 모든 고객을 방문함
            # 마지막 고객집에서 집으로 가능 경로 더해주기
            dist += abs(x-home[0]) + abs(y-home[1])
            if dist < min_dist: # 누적 이동거리가 최소이면 저장,
                min_dist = dist
            return
        # 현재 방문가능한 모든 고객 방문해보기
        for i in range(N):
            #방문하지 않은 고객 방문하기
            if not visited[i]:
                visited[i] = 1
                tmp = abs(x-cust[i][0]) + abs(y-cust[i][1])
                solve(idx+1,dist+tmp,cust[i][0],cust[i][1])
                visited[i] = 0

    solve(0,0,comp[0],comp[1])
    print("#{} {}".format(tc,min_dist))