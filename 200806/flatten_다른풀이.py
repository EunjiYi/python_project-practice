# 평탄화
T = 10
for tc in range(1,T+1):
    N = int(input())
    area = list(map(int,input().split()))

    for i in range(N):
        max_idx = 0
        min_idx = 0
        max_v = area[0]
        min_v = area[0]
        for j in range(len(area)):
            #최대값 위치, 최소값 위치
            if area[j] > max_v:
                max_idx = j
                max_v = area[j]

            if area[j] < min_v:
                min_idx = j
                min_v = area[j]

        area[max_idx] -= 1
        area[min_idx] += 1
    # 평탄화 작업완료
    max_idx = 0
    min_idx = 0
    max_v = area[0]
    min_v = area[0]
    for j in range(len(area)):
        # 최대값 위치, 최소값 위치
        if area[j] > max_v:
            max_idx = j
            max_v = area[j]

        if area[j] < min_v:
            min_idx = j
            min_v = area[j]

    print("#%d"% tc, max_v - min_v)
