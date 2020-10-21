# 거듭제곱: 밑수와 제곱수를 입력받아서 결과를 반환하는 함수작성

def power(base, exponent):
    if exponent == 0:
        return 1

    # exponent 제곱수가 짝수일 때
    if exponent % 2 == 0:
        new_base = power(base, exponent//2)
        return new_base * new_base

    # exponent 제곱수가 홀수일 때
    else:
        new_base = power(base, (exponent - 1) // 2)
        return new_base * new_base * base

result = power(2, 8) # 2의 8제곱을 구하라
print(result)

