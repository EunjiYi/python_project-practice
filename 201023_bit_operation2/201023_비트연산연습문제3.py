### 연습문제3
# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. 암호는 연속되어 있다.

# 입력예시
# 0DEC

# 출력예시
# 00 001101 111011 00 -> 0 2가 출력된다.


# 암호비트패턴은 아래와 같다.
pattern = [[0,0,1,1,0,1], #-> 0
           [0,1,0,0,1,1], #-> 1
           [1,1,1,0,1,1], #-> 2
           [1,1,0,0,0,1], #-> 3
           [1,0,0,0,1,1], #-> 4
           [1,1,0,1,1,1], #-> 5
           [0,0,1,0,1,1], #-> 6
           [1,1,1,1,0,1], #-> 7
           [0,1,1,0,0,1], #-> 8
           [1,0,1,1,1,1]] #-> 9

def hex_to_decimal(c):
    num = ord(c)
     # 숫자
    if 48 <= num <= 57:
        return num - 48
    elif 65 <= num <=70:
        return num - ord('A') + 10

def decimal_to_binary(n):   # 0~15
    binary = [0] * 4    # 0~15까지는 4개의 비트로 처리가능
    idx = 3
    while n > 0:
        # n을 2로 나누어서 나머지를 계속 저장
        binary[idx] = n % 2
        idx -= 1
        n = n//2
    return binary

# print(decimal_to_binary(15))
#  0000000 1   01
str = "0DEC"
result = list()
for i in range(len(str)):
    number = hex_to_decimal(str[i])
    result += decimal_to_binary(number)

for i in range(len(result)):
    tmp = result[i:i+6]
    if tmp in pattern:
        for j in range(i,len(result),6):
            password = result[j:j+6]
            if len(password ) == 6:
                print(pattern.index(password),end=" ")
        break   #바깥쪽 반복문 종료
