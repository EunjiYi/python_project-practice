T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    #idx: 정류장 번호
    #cnt : 배터리 교환횟수
    #remain : 배터리 잔량
    min_cnt = 0xffffffff
    def backtrack(idx,cnt,remain):
        global min_cnt
        remain -= 1 # 배터리를 사용했으니 잔량 1감소
        if idx == N:
            if cnt < min_cnt:
                min_cnt = cnt
            return
        if cnt >= min_cnt:
            # 중간 배터리 교환 횟수가 최소 교환 횟수보다 크거나 같으면 진행 X
            return

        #배터리를 교환하는 경우
        backtrack(idx+1,cnt+1,arr[idx])
        #배터리를 교환하지 않는경우, 배터리 잔량이 남아있어야만, 교환하지 않음
        if remain > 0:
            backtrack(idx+1,cnt,remain)

    backtrack(2,0,arr[1])
    print("#{} {}".format(tc,min_cnt))