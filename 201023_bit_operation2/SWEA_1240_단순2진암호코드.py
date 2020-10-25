## 바보다 앞에서 부터 찾아서 1나올때 까지 하지 말고
# 뒤에 부터 찾아서 1나올 때까지 하면, try except 안써도 되는데 ㅜ
# 왜냐면 현재 dic에 들어있는 코드들이 전부 끝에 1로 끝나기 때문에 맨 뒤에서 부터 1 나올 때 까지 
# 2중 for 문 돌리다가.  거기서 부터 행 = i -4 / 열 = j -55 하면 딱 코드 56개만 뽑힘...ㅎㅎ
# 바보다 바보야 

dic = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9,
       }
def isCode(arr): # 2차원 배열 arr에 담긴 것이 올바른 암호코드이면 True, 아니면 False를 반환하는 함수
    global result
    number = [0] * 8

    for i in range(8):
        try:
            number[i] = dic[''.join(map(str, arr[i]))] # 만약 dic에 숫자가 없어서 KeyError가 나면, except 실행
        except:
            return False
        else: # 예외 발생하지 않았으면 숫자는 있는 것. 이 숫자가 올바른지 체크한다.
            continue

    if ( (number[0]+number[2]+number[4]+number[6]) * 3 + (number[1]+number[3]+number[5]) + number[7] ) % 10 == 0:
        result = sum(number)
        return True
    else:
        return False

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]

    # 해당 줄에 1이 하나라도 있으면 그 줄이 암호시작줄.
    row = 0
    for i in range(N):
        for j in range(M):
            if code[i][j]:
                row = i #암호시작 행을 저장
                break
        if row:
            break

    # row줄의 몇 번 인덱스부터 암호인지 모르니까 맨 처음부터 슬라이싱해서 완전탐색.
    flag = False
    result = 0
    for x in range(0, M-56+1):
        tmp = []
        for c in range(0, M-7+1, 7):
            tmp.append(code[row][x+c:x+c+7])
        flag = isCode(tmp) #tmp가 올바른 암호코드인지 체크.
        if flag:
            break

    print("#{}".format(tc), end = ' ')
    if flag:
        print("{}".format(result))
    else:
        print(0)