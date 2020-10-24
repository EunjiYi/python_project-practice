# def perm(k): #k만 있으면 n이 클 때 시간초과 나옵니다.
#     #cur_sum: 0 ~k-1행까지 선택한 값들의 합을 넣어주자. 누적시켜서 넘기기
#     if k == N:
#         S = 0
#         for r, c in enumerate(cols):
#             S += arr[r][c]
#         global ans
#         ans = min(ans, S)
#     else:
#         for i in range(k, N):
#             cols[k], cols[i] = cols[i], cols[k]
#             perm(k+1)
#             cols[k], cols[i] = cols[i], cols[k]
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cols = [i for i in range(N)]
#     ans = 0xfffffff
#     perm(0)
#     print(ans)
#======================cur_sum 넣은 것 ------------------

def perm(k, cur_sum): #k만 있으면 n이 클 때 시간초과 나옵니다.
    #cur_sum: 0 ~k-1행까지 선택한 값들의 합을 넣어주자. 누적시켜서 넘기기
    global ans
    
    # 가지치기 = 이거 안 넣으면 n 클 때 시간초과남.
    if ans <= cur_sum: return

    if k == N:
        #S = 0
        # for r, c in enumerate(cols):
        #     S += arr[r][c]
        # print(S, cur_sum) # 당연히 이 두 개가 같음.

        # ans = min(ans, S)
        ans = min(ans, cur_sum)
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k+1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = [i for i in range(N)]
    ans = 0xfffffff
    perm(0, 0)
    print(f'#{tc} {ans}')