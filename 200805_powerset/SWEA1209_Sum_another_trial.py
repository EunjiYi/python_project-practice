# 가로 세로 대각 총합중 최대값 출력
import sys
sys.stdin = open("input.txt","r")
T = 10
for tc in range(1,T+1):
    tn = int(input())
    #input().split() :  "1 2 3 4 5"  >> ['1','2','3','4','5']
    numbers = [list(map(int, input().split())) for _ in range(100)]
    #가로 합, 세로합,대각합(위) 대각합(아래) 을 저장하는 배열
    max_number = [0]*4
    #가로합
    for i in range(len(numbers)):
        row_sum = 0
        for j in range(len(numbers[i])):
            row_sum += numbers[i][j]
            #반복문안에서는 합
        #반복이 끝나면, 가로합의 최대값 구하기( 이전 최대값과 비교)
        if max_number[0] < row_sum:
            max_number[0] = row_sum

    #세로합
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += numbers[j][i]
        if col_sum > max_number[1]:
            max_number[1] = col_sum

    # 대각합 (상)
    for i in range(100):
        for j in range(100):
            if i+j == 99:
                max_number[2] += numbers[i][j]
    # 대각합 (하)
    for i in range(100):
        for j in range(100):
            if i==j:
                max_number[3] += numbers[i][j]

    result = max_number[0]
    #총 합 가운데 최대값 찾기
    for i in range(len(max_number)):
        if result < max_number[i]:
            result = max_number[i]

    print("#%d" %tn, result)
