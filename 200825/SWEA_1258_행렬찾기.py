import sys
sys.stdin = open("input.txt","r")
#행렬찾기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    #matrix 순회 하면서 영역 찾고, 찾은 영역은 0으로 변환
    bottles = list()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                #영역 시작 >>>약품이 놓인 영역 검사
                #서브매트릭스 영역 검사 : 0이 나오거나 영역이 끝날때 까지
                row = 0
                col = 0
                for k in range(i,N):
                    if matrix[k][j] == 0:
                        break
                    else:
                        row += 1
                for k in range(j,N):
                    if matrix[i][k] == 0:
                        break
                    else:
                        col += 1
                # 찾은 영역의 내용을 0으로 바꿔줌
                for k in range(i,i+row):
                    for l in range(j,j+col):
                        matrix[k][l] = 0
                bottles.append((row*col,row,col))

    #영역검사 끝, 출력
    # 영역이 작은순, 행이 작은순
    #정렬 > bottles
    for i in range(len(bottles)):
        for j in range(len(bottles)-i-1):
            if bottles[j][0] > bottles[j+1][0]: # 영역의 크기가 크면 뒤로
                bottles[j], bottles[j+1] = bottles[j+1], bottles[j]
            elif bottles[j][0] == bottles[j+1][0]: # 영역의 크기가 같다면
                if bottles[j][1] > bottles[j+1][1]: #행 길이 비교
                    bottles[j], bottles[j + 1] = bottles[j + 1], bottles[j]
    print("#{}".format(tc), end=" ")
    print(len(bottles), end=" ")
    for i in range(len(bottles)):
        print(bottles[i][1], bottles[i][2], end=" ")
    print()




