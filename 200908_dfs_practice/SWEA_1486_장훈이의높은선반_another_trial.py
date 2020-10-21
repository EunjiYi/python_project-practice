def tower(idx,tmp_sum):
    global min_height
    if tmp_sum > min_height:
        return
    if idx == N:
        #키의 합이 B가 넘는 경우에만 정답 후보
        if tmp_sum >= B and min_height > tmp_sum:
            min_height = tmp_sum
        return
    #idx에 해당하는 요소를 부분집합에 포함하거나/안하거나
    tower(idx+1,tmp_sum + heights[idx])
    tower(idx + 1, tmp_sum)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    INF = float("inf")
    min_height = INF
    tower(0,0)
    print("#{} {}".format(tc,min_height-B))

