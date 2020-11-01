import sys
sys.stdin = open('123.txt', 'r')

dic2 = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}
# 16진수 num을 4자리 2진수로 바꾸는 함수
def hex_to_binary(num):
    if num in dic.keys():
        num = dic[num]
    else:
        num = int(num)
    bit = [0, 0, 0, 0]
    idx = 3
    while num > 0:
        bit[idx] = num % 2
        num = num // 2
        idx -= 1

    bit = list(map(str, bit))

    ret = ''
    for b in bit:
        ret += b
    return ret


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    #print(matrix)


    # 0이 아닌 줄만 가져오는 코드 생략
    # 이게 빠르다고 생각했는데, 맨 뒤부터 하나씩 0아닌것 찾아오느니, 그 시간에 전체를 다 순회하면서 16진수로 바꾸는 게 빨랐다.
    binary_not_zero = [''] * n
    for i in range(len(matrix)):
        for j in range(m):
            binary_not_zero[i] += hex_to_binary(matrix[i][j])

    result = 0
    number = []
    check = [] # 8번에서 막힌 이유 ㅠㅠ 중복체크시 합이 같은 걸 제외하면 안되고 문자코드가 같은 걸 중복체크해야한다.
    # 그래서 체크 배열 만들었다.
    for r in range(len(binary_not_zero)):
        r2 = r3 = r4 = 0
        for i in range(m*4-1, -1, -1):  # 각 줄 별로 만족하는 정상코드의 합을 result에 누적한다.
            if r3 == 0 and r2 == 0 and binary_not_zero[r][i] == '1':
                r4 += 1
            elif r4 and r2 == 0 and binary_not_zero[r][i] == '0':
                r3 += 1
            elif r4 and r3 and binary_not_zero[r][i] == '1':
                r2 += 1
            ## 여기까지 하나의 코드 다 구함. 가장 앞의 0은 갯수 몰라도 dic2에서 찾을 수 있음.
            if r2 and r3 and r4 and binary_not_zero[r][i] == '0':
                rmin = min(r2, r3, r4)
                r2 = r2 // rmin
                r3 = r3 // rmin
                r4 = r4 // rmin
                num = dic2[(r2, r3, r4)]
                number.insert(0, num)
                # print(number)
                r2 = r3 = r4 = 0

            tmp1 = tmp2 = 0
            if len(number) == 8:
                for i in range(len(number)):
                    if i % 2 == 0:
                        tmp1 += number[i]
                    else:
                        tmp2 += number[i]
                sum_v = tmp1 * 3 + tmp2
                if sum_v % 10 == 0 and number not in check: #체크배열 검사
                    result += sum(number)

                # number의 정상코드 유무와 상관없이 검사한 것은 다 check에 넣는다.
                # 이걸 if문 안에 넣어서 고생했다 ㅠ
                check.append(number)

                # 초기화
                number =[]

    print("#{} {}".format(tc, result))