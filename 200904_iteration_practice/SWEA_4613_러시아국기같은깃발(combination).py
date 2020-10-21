def comb(idx, count):
    global white_region, blue_region
    if count == 2:  # 필요한 개수만큼 선택함
        check = False
        for i in range(len(selected)):
            if selected[i] and not check:
                white_region = i
                check = True
            elif selected[i] and check:
                blue_region = i
                break
        counting()
        return
    if idx >= N-1:  # 가장 마지막줄은 빨간색놔야하니까. 마지막줄 바로 전까지만!! 조심!
        return

    # 요소의 포함/미포함 여부 결정
    selected[idx] = 1
    comb(idx + 1, count + 1)
    selected[idx] = 0
    comb(idx + 1, count)


def counting():
    global mcnt, white_region, blue_region
    cnt = 0
    # 흰색 영역 순회하면서, 흰색이 아닌 칸 세기
    for w_row in range(white_region + 1):
        for w_col in range(M):
            if flag[w_row][w_col] != 'W':
                cnt += 1
    # 파란색 아닌 칸 세기
    for b_row in range(white_region + 1, blue_region + 1):
        for b_col in range(M):
            if flag[b_row][b_col] != 'B':
                cnt += 1
    # 빨간색 아닌 칸 세기
    for r_row in range(blue_region + 1, N):
        for r_col in range(M):
            if flag[r_row][r_col] != 'R':
                cnt += 1
    if cnt < mcnt:
        mcnt = cnt

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    mcnt = float('inf')
    selected = [0] * N

    comb(0, 0)

    print("#{} {}".format(tc, mcnt))