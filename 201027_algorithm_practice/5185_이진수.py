def hex_to_decimal(c):
    #아스키코드 16진수
    num = ord(c) #내장함수 사용.
    if 48 <= num <= 57:
        return num - 48
    elif 65 <= num <=70:
        return num - ord('A') + 10

def decimal_to_binary(n):
    binary = [0] * 4
    idx = 3
    while n > 0:
        binary[idx] = n % 2 # 2로 나눈 나머지를 계속 저장한다.
        idx -= 1
        n = n//2
    return binary

for tc in range(1, int(input()) + 1):
    n, hex = input().split()
    #print(hex)

    result = []
    for h in hex:
        number = hex_to_decimal(h)
        #print(number)
        result += decimal_to_binary(number)

    print("#{}".format(tc), end = ' ')
    for i in range(len(result)):
        print(result[i], end = '')
    print()


