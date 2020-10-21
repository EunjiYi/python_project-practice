## 선택정렬하면 100점 나오고 버블정렬하면 80점이 나온것은 예제상의 우연...
# 버블 정렬은 정렬과정에서 앞뒤 요소의 위치가 많이 바뀌는데
# 작성하신 선택정렬은 앞뒤 요소의 위치가 많이 바뀌지 않아서
# 우연히 정답이 나온듯 합니다.

# 사실 두 코드 모두 "크기가 같을 경우 행이 작은 녀석이 앞쪽이다." 라는 조건이 빠짐
# 테스트케이스상 우연히 선택정렬이면 되었던 것... ㅠ,ㅠ
# (사실 아직도 이해는 안간다만, 내 코드가 완벽하지 않았던 것은 사실이다.)

#원래 구현했던 버블정렬에 아래 조건을 추가하니까 PASS 나옴.
'''
elif area[j][2] == area[j + 1][2] and area[j][0] > area[j + 1][0]:
area[j], area[j + 1] = area[j + 1], area[j]
'''

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    area = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:

                #가로, 세로 길이 구하는거 시작
                x = 0 #가로길이
                for k in range(j,n):
                    if matrix[i][k] != 0:
                        x += 1
                    else:
                        break
                y = 0
                for k in range(i,n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break

                #  check -> 따로 2차원배열 만들필요 없음.
                for k in range(i,i+y):
                    for l in range(j,j+x):
                        matrix[k][l] = 0

                area.append((y,x,y*x))



    #print(area) #결과나옴

    #작은순으로 정렬
    for i in range(len(area)-1, 0, -1):
        for j in range(0, i):
            if area[j][2] > area[j+1][2]:
                area[j], area[j + 1] = area[j + 1], area[j]
            # 이거 추가
            elif area[j][2] == area[j + 1][2] and area[j][0] > area[j + 1][0]:
                area[j], area[j + 1] = area[j + 1], area[j]

    print('#{} {}'.format(tc, len(area)), end =" ")

    for i in range(len(area)):
        for j in range(2):
            print(area[i][j], end = " ")
    print()






