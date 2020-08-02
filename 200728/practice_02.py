# list method 이용
def sum_of_repeat_number(numbers):
    result = 0
    for num in numbers:
        if numbers.count(num) == 1:  #count()쓰니까 간단.
            result += num
    return result


## 아래는 생각도 못함.
'''
def sum_of_repeat_number(numbers):
    once = []   #한 번만 나온거 저장하는 곳
    multi = []  # 두 번 이상 나온거 저장하는 곳
    for num in numbers:
        if num not in multi and num not in once:
            once.append(num)  #새로운 것 && 두 번 이상 안나온 것
        elif num not in multi and num in once:
            once.remove(num) #한번 카운트 됐는데 또 나온것을 삭제
            multi.append(num) #여기에 추가
    return sum(once)  #sum쓰면 간단
'''

print(sum_of_repeat_number([4, 4, 7, 8, 10]))  #25
print(sum_of_repeat_number([4, 4, 2, 3, 1]))  #6