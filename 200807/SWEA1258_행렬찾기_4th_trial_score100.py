T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    mylist = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j]: #0이 아니면 = 순회해야할 값이 있으면
                # 가로, 세로 길이 구하자
                x = 0  # 가로길이(column)
                for k in range(j, N): #0이 아니면 = 순회해야할 값이 있으면
                    if matrix[i][k]: #row는 고정한 상태에서 column만 N-1까지 인덱스 변경
                        x += 1
                    else:
                        break
                # 세로길이(row)
                y = 0
                for k in range(i, N):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break

                # 표시한 영역은 0으로 다 바꾸기 - 채크 매트릭스를 별도로 만들 필요가 없었다...ㅠ
                for k in range(i, i + y):
                    for l in range(j, j + x):
                        matrix[k][l] = 0
                mylist.append((y, x, x * y))

                #강사님 로직이 완전히 나랑 같다. 다만 내가 구현할 때 값이 없으면(0이면) 다시 되돌아가도록 구현해서,
                #index out of range가 났던 것.

    #정렬하기 - x*y가 작은 순으로 선택정렬
    for i in range(len(mylist) - 1):
        idx = i #시작점잡기
        for j in range(i + 1, len(mylist)):
            if mylist[idx][2] > mylist[j][2]:
                idx = j
        mylist[i], mylist[idx] = mylist[idx], mylist[i]

    print(f'#{tc} {len(mylist)}', end=' ')  # f스트링 왜 먹지 신기해

    for i in range(len(mylist)):
        for k in range(2):
            print(f'{mylist[i][k]}', end=' ')
    print()