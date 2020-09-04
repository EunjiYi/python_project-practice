T = int(input())
for tc in range(1,T + 1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    mcnt = float('inf')   # 최솟값 = 답

    #흰색 영역: 0행 ~ 끝에서 3행까지
    for white_region in range(0, N-2):
        #파란색 영역: 흰색 다음부터 끝에서 2행까지
        for blue_region in range(white_region+1, N-1):
            # 바꾸어야 할 개수 cnt
            cnt = 0
            # 흰색 영역 순회하면서, 흰색이 아닌 칸 세기
            for w_row in range(white_region+1):
                for w_col in range(M):
                    if flag[w_row][w_col] != 'W':
                        cnt+= 1
            # 파란색 아닌 칸 세기
            for b_row in range(white_region+1, blue_region+1):
                for b_col in range(M):
                    if flag[b_row][b_col] != 'B':
                        cnt += 1
            # 빨간색 아닌 칸 세기
            for r_row in range(blue_region+1, N):
                for r_col in range(M):
                    if flag[r_row][r_col] != 'R':
                        cnt+=1
            if cnt < mcnt:
                mcnt = cnt

    print("#{} {}".format(tc,mcnt))