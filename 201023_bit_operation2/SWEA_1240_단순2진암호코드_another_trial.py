code = { (3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9,
}

T = int(input())
for tc in range(1,T+1):
    N, M  = map(int, input().split())
    board = [input() for _ in range(N)]
# board 에서 암호코드를 읽어서 결과를 반환하는 함수
# 암호코드의 합 또는 0을 반환
    def solve():
        # 열의 뒤쪽 부터검사 시작 : 모든 암호의 끝은 1로 끝이남.
        # 부분만 있는 암호가 없기때문에 1을 찾으면 연속된 8개의 숫자를 찾을 수 있다.
        for i in range(N):
            for j in range(M-1,-1,-1):  #열을 뒤쪽 부터 검사
                if board[i][j] == '0':
                    continue  #0이라면 암호 시작이 아님 continue
                # 암호시작, 암호의 개수는 총 8개
                idx = j
                pwd = list()
                for k in range(8):
                    n1 = n2 = n3 = n4 = 0   #암호의 각 구성을 세기 위한 변수
                    #0101
                    while board[i][idx] == '1':
                        n4 += 1
                        idx -= 1
                    while board[i][idx] == '0':
                        n3 += 1
                        idx -= 1
                    while board[i][idx] == '1':
                        n2 += 1
                        idx -= 1
                    n1 = 7 - (n2 + n3 + n4)
                    idx -= n1   #n1 인덱스 수정
                    pwd.append(code[(n1,n2,n3,n4)])
                # 정상적인 암호인지 검사
                sum_even = pwd[2] + pwd[4] + pwd[6]
                sum_odd =  pwd[1] +pwd[3] + pwd[5] + pwd[7]
                tmp = sum_odd*3 + sum_even + pwd[0]
                if tmp % 10 == 0:
                    return sum_odd + sum_even + pwd[0]
                else:
                    return 0

    result = solve()
    print("#{} {}".format(tc,result))