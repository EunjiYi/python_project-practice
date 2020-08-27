# import sys
# sys.stdin = open("../Day5_200826_stack/input.txt", "r")

def check_pal(M):
    # 회문의 길이를 입력받아서 해당 길이의 회문이 있는지 없는지 판단
    for i in range(100):
        for j in range(100-M+1):
            #회문검사
            #회문검사 대상 추출
            tmp = board[i][j:j+M]  #가로회문 검사대상
            tmp2 = zboard[i][j:j+M]    #세로회문검사 대상
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return True
    return False

T = 10
for x in range(T):
    tc = int(input())
    board = [input() for _ in range(100)]
    zboard = list(zip(*board))
    #가로에 있는 회문이 있는지 검사
    #전치행렬의 가로 검사를 하면, 원래 행렬의 세로 검사와 같다.
    #가장 긴 회문을 찾으면 되니까, 긴 것부터 검사를 하면된다.
    result = 0
    for i in range(100,0,-1):
        if check_pal(i):
            result = i
            break

    print("#{} {}".format(tc,result))