T = int(input())
for tc in range(1,T+1):
    N = int(input())
    costs =[list(map(int,input().split())) for _ in range(N)]
    used = [0]* N
    min_cost = 0xfffffffff
    def solve(idx,cost):
        global min_cost
        if idx == N:
            if cost < min_cost:
                min_cost = cost
            return
        if cost >= min_cost:
            return
        for i in range(N):
            if not used[i]:
                used[i] = 1
                solve(idx + 1, cost+costs[idx][i])
                used[i] = 0
    solve(0,0)
    print("#{} {}".format(tc,min_cost))