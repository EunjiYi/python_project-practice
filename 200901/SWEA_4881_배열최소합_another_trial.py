def backtrack(idx,sum_v):
    global min_sum
    if idx == N:
        #모든 행에서 숫자하나씩 선택한 상황이다
        #최소합 비교
        if min_sum > sum_v:
            min_sum = sum_v
        return

    for i in range(N):
        if not selected[i]:  #selected[i] == 0
            selected[i] = 1 # 현재 열 사용 표시

            tmp = sum_v+arr[idx][i]
            if tmp < min_sum:
                backtrack(idx+1,tmp)    #다음행으로 진행
            selected[i] = 0 # 현재열 사용 표시 해제


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    selected = [0] * N
    #구할 값은 최소합:
    min_sum = 100
    backtrack(0,0)
    print("#{} {}".format(tc,min_sum))


