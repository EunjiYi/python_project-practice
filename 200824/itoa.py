# itoa()
# 123 > "123"
# 단, str()함수 x, list()x
# 숫자 하나하나를 따로 떼어내야한다.

# 123 -> 3 2 1 순을 빼내자
# 숫자를 하나씩 분리할 때는 % modular 연산을 사용한다.
# 123 // 10 > 12
# 123 & 10 > 3

# 123 -> 1 2 3 순으로 빼내기
# 123 % 100 > 23  -> 이건 사전에 100이란 수를 알아야하기 때문에 뒤에서부터 뽑아내는 것이 좀 더 쉽다.
# 123 //100 > 1
# 23 % 10 > 3
# 23 // 10 > 2
# 3 % 1 > 0
# 3 // 1 > 3

def itoa(number):
    #해야할 일: 숫자를 한 자리씩 잘라서 문자열로 만들기
    # 123 >  123//100,  23//10,  3//1
    # 자리수를 알아야한다.
    # 대상수가 0이 될 때까지 반복한다.

    divider = 1
    result = ""
    # divider 구하기
    while True:
        tmp = divider * 10
        if tmp > number:
            break
        divider = tmp

    # divider를 구했으니 숫자를 나눠주자
    while number > 0:
        quotient = number // divider
        remainder = number % divider
        divider =  divider // 10

        # 몱을 문자열로 만들어서 더해주기
        result += chr(quotient + ord('0')) #아스키코드 활용
        number = remainder
    return result


a = 12345
b = itoa(a)
print(b)
print(b[2])