# atoi 함수 만들기 : 숫자형태의 문자열 을 받아서 숫자로 변경
# atoi('1234') >> 1234
#['1','2','3','4']
# '1' >> 0 * 10 +  1 >> 1
# '2' >> 2, 1*10 + 2 > 12
# '3' >> 3, 12*10 + 3 >> 123
# '4' >> 4 123* 10 + 4 >> 1234
def atoi(str):
    result = 0
    is_negative = False

    for i in range(len(str)):
        if i==0 and str[i]== '-':
            is_negative = True
            continue
        result *= 10    # result = result * 10
        #str[i] 문자형태의 데이터를 숫자로 변경
        #str[i] >> '1' >> 아스키코드의 숫자를 이용해서 숫자로 변환
        #'1'이라는 문자의 아스키 코드는 10진수 49
        # 49 - 48 : 1   ord('1') : '1' 이라는 문자의 아스키 코드를 반환
        tmp = ord(str[i]) - ord('0')
        result += tmp
    if is_negative: # 참이면 음수
        result = -result
    return result

a = '-3456'
b = atoi(a)
print(b+1)


