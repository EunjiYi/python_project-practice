#몫과 나머지 이용 - 내 방법
def sum_of_digit(number):
    sumsum = 0
    while number > 0:
        sumsum += number % 10
        number = number // 10
    return sumsum



print(sum_of_digit(1234)) #=> 10
print(sum_of_digit(4321)) #=> 10