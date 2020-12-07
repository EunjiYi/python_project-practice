for tc in range(1, int(input()) + 1):
    d1, m1, m3, y1 = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    #print(plan)
    cost = [0] * 13 # cost = 1월부터 그 달'까지' 이용하는데 드는 최소비용
    #print(cost)

    for i in range(1, 13): # 1월부터 12월
        choice1, choice2 = 10000000000, 10000000000
        if i >= 1:
            # (1) i-1월의 최소비용 + min(1일권*이용일, 1개월 권)
            choice1 = cost[i-1] + min(d1*plan[i], m1)
        if i >= 3:
            # (2) i-3월의 최소비용 + 3개월 권
            choice2 = cost[i-3] + m3

        # (1), (2) 중 작은 것을 cost에 넣는다.
        cost[i] = min(choice1, choice2)

    #여기까지만 하고 cost[12]를 찍으면 테스트케이스 50개 중 47개만 돈다.
    # print("#{} {}".format(tc, cost[12]))
    #그 이유는 12월까지 이용할 금액과, 1년 이용권을 비교 안해서!!!
    ans = min(cost[12], y1)
    print("#{} {}".format(tc, ans))

