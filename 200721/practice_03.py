numbers = [26, 39, 51, 53, 57, 79, 85]

# 아래에 코드를 작성하시오.
for number in numbers:
    cnt = 0
    for num in range(2, number):
        if number % num == 0:
            print(f"{number}은(는) 소수가 아닙니다. {num}은(는) {number}의 인수입니다.")
            cnt += 1
            break
    if cnt == 0:
        print(f"{number} 소수입니다.")



#39은(는) 소수가 아닙니다. 3은(는) 39의 인수입니다.
#79은(는) 소수입니다