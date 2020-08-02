number = int(input())

# 아래에 코드를 작성하시오.
for i in range(2, number):
    if number % i == 0:
        print('N')
        break;
    else:
        print('Y')
        break;

# 입력 19 -> 출력 Y