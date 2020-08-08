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

    print('#{} {}'.format(tc, len(area)), end =" ")

    for i in range(len(area)):
        for j in range(2):
            print(area[i][j], end = " ")
    print()






