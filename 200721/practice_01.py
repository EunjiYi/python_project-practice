number = int(input())

# 아래에 코드를 작성하시오.
result = 0
for num in range(1, number+1):
    if num % 2 == 0: #짝수이면
        result += num * 3
    else:
        result += num * 2
print(result)

# 입력 5 -> 출력 36