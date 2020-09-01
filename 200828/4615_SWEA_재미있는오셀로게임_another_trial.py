# import sys
# sys.stdin = open("input.txt")
# 오셀로
def init():
    st = N // 2
    board[st][st] = board[st + 1][st + 1] = 2
    board[st][st + 1] = board[st + 1][st] = 1



dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def change(c,r,color):
    #돌을 놓았을 때 영향을 미치는 곳의 돌색깔 바꾸기
    #8방향을 검사한다.
    #영역을 벗어나기 전(또는 빈칸)까지 검사하면서, 나랑 같은 돌이 나올때 까지 진행하고
    #같은 돌이 나오면, 되돌아 오면서 색깔을 바꾼다.
    board[r][c] = color
    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            #범위 벗어나는 경우, 비어있는 칸을 만나면
            if nr <= 0 or nc <= 0 or nr > N or nc > N or board[nr][nc] ==0 :
                break
            # 범위내에 있는데, 나랑 똑같은 색깔을 찾았으면
            if board[nr][nc] == color:
                #그 위치부터, 원래 위치 까지 되돌아 오면서 내색깔로 바꿔줌
                while not (nr == r and nc == c): # 원래 자리로 돌아 올때 까지
                    nr -= dr[d]
                    nc -= dc[d]
                    board[nr][nc] = color
                break   # 바깥쪽 while 종료


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    board = [[0]*(N+1) for _ in range(N+1)]
    #초기돌의 위치
    init()

    for i in range(M):
        c,r,color = map(int,input().split())
        change(c,r,color)   #색깔 바꾸기
    b_cnt = 0
    w_cnt = 0
    for row in board:
        b_cnt += row.count(1)
        w_cnt += row.count(2)
    print("#{} {} {}".format(tc,b_cnt,w_cnt))




