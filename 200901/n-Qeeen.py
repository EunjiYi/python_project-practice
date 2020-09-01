#NxN 크기의 체스판에 퀸을 N개 배치
# 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수 구하라.


N = 10
#보드에 놓인 퀸이 영향을 미치는 곳을 표시하기 위한 배열
check = [[0] * N for _ in range(N)]
cnt = 0
def marking(r,c,num):
    # r,c에 놓여진 퀸에 의해 영향받는 칸에 num을 더해주는 함수
    # num은 1 또는 -1
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 > nr or 0 > nc or nr >= N or nc >= N:
                break
            check[nr][nc] += num

# 각 행에서 어느 칸에 퀸이 놓여질지 검사
def n_queen(r):
    global cnt
    # 그 행에서 퀸이 놓일 자리가 결정되면 다음행으로 진행
    # 만약에 마지막 행까지 퀸을 놓게되면, 모든 행에 퀸을 놓은것
    # N개의 퀸을 놓은 것이기 때문에. 해를 찾은 것이 된다.
    if r >= N: # r = 행
        cnt += 1
        return

    for i in range(N): #어떤 칼럼에 퀸을 놓을지 검사
        if check[r][i] == 0: # 표시가 안된자리는 퀸을 놓을 수 있다.
            # 만약에 현재 칸에 퀸을 놓을 수 있으면, 퀸을 놓고
            # r,i에 퀸을 놓고, 그 퀸에 의해 영향 받는 칸에 표시(+1)
            # 다음 행으로 진행
            marking(r,i,1)
            n_queen(r+1)

            # n_qeen(r+1)을 해서 marking을 하고 n_queen(r+2)을 시작했는데  0인 칸이 없었다면 = 즉 r+1에 퀸을 놓는 것이 틀린 것.
            # if check[r][i] == 0:를 돌지않아서 return 됨. 즉 n_queen(r+1)로 다시 돌아옴.
            # 그 r+1이 현재 상황에서는 r이니까, 그 r, i로 인해 마킹된 곳을 지워야한다. (즉, n_queen(r+1)이 makring한 곳)
            # 지우는 법은 -1헤줘서 다시 되돌리기.
            # 즉 r+1이 잘못되어서 r+1의 영향력(마킹)을 되돌린 것이다. 그 전 퀸인 r의 영향력은 그대로 살아있음.
            marking(r, i, -1)
    # 반복문이 끝나면 더이상 검사할 대상이 없기 때문에 종료
    return

n_queen(0)
print(cnt)

# 지수함수시간이 걸리기 때문에 시간이 오래 걸리는 편
# 10 넣으면 724나오기까지 좀 걸림