
def getResult():
    for i in range(0, len(string)-1, 3):

        #카드숫자를 number에 int로 저장
        if string[i+1] == '0':
            number = int(string[i+2])
        else:
            numberlist = []
            numberlist.append(string[i + 1])
            numberlist.append(string[i + 2])
            number = int("".join(numberlist))

        # 모양 체크
        if string[i] == 'S':
            if not checked[0][number]:
                checked[0][number]  = 1
            else:
                return 'ERROR'
        elif string[i] == 'D':
            if not checked[1][number]:
                checked[1][number]  = 1
            else:
                return 'ERROR'
        elif string[i] == 'H':
            if not checked[2][number]:
                checked[2][number]  = 1
            else:
                return 'ERROR'
        else:
            if not checked[3][number]:
                checked[3][number]  = 1
            else:
                return 'ERROR'

    for i in range(4):
        result[i] = checked[i].count(0) - 1

T = int(input())
for tc in range(1, T + 1):
    string = input()
    checked = [[0] * 14 for _ in range(4)]
    result = [0] * 4
    # 0열 = S
    # 1열 = D
    # 2열 = H
    # 3열 = C

    ret = getResult()

    print(f'#{tc}', end = " ")
    if ret:
        print('ERROR')
    else:
        for i in range(4):
            print(f'{result[i]}', end = " ")
        print()