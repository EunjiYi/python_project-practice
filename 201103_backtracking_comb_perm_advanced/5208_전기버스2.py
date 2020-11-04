def comb(idx, cnt, sum):
    # idx는 정류장 번호, cnt: 충전 횟수, sum: 지금 충전된 양
    # 재귀돌리니까 함수 내에서는 당장 지금 상황만 따지면 됨.
    global mcnt

    if cnt >= mcnt: # 꼭 쓰기. 없으면 시간초과
        return

    if idx >= n-1: # 여기서 마지막 정류장일 때 바로 리턴되니까 마지막 정류장에서 충전유무 고려 안함.
        if cnt < mcnt:
            mcnt = cnt
            return

    if sum <= 0:  # 충전된게 없으면 무조건 충전
        comb(idx+1, cnt+1, stop[idx]-1) #여기서 조심할 것이 sum+stop[idx]-1이 아니다!! 그냥 교체하는거라서 잔량 의미 없음.
    elif sum >= stop[idx]: # 지금 충전되어있는 양이, 이번 정류장에서 충전할 수 있는 양보다 많다면(같은 것 포함), 굳이 충전 안 해도 된다.
        comb(idx+1, cnt, sum-1)
    else: #sum < stop[idx] and sum > 0: # 지금 충전되어있는 양이, 이번 정류장에서 충전할 수 있는 양보다 적다면, 충전해도되고 안해도됨.
        comb(idx+1, cnt+1, stop[idx]-1)
        comb(idx+1, cnt, sum-1)


for tc in range(1, int(input())+1):
    tmp = list(map(int, input().split()))

    n = tmp[0]
    #print(n)
    stop = tmp[1:]
    #print(stop)

    mcnt = 10000000000000000000000
    comb(1, 0, stop[0]-1) #처음 충전은 횟수에 포함 안되니까 처음부터 넣고 시작. -1해주는 이유는 한 정류장 이동 했으니까.
    # 처음에 넣고 시작하니까 0번 정류장은 볼 필요없고 바로 1정류장부터 충전할지말지 신경쓰면 됐됐다 ㅠㅠ 이거 찾는데 오래걸림

    print("#{} {}".format(tc, mcnt))
