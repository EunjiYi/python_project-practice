import sys
sys.stdin = open('123.txt', 'r')

def two_decimal():
    two_numbers = []
    for i in range(len(two)):
        two[i] = two[i] ^ 1
        #print(two[i])

        # 2진수를 10진수로 변환
        two_number = 0
        for j in range(len(two) -1, -1, -1):
            two_number += two[j] * (2 ** (len(two) -1 - j))
        two_numbers.append(two_number)

        two[i] = two[i] ^ 1

    return two_numbers

def three_to_ten():
    # 3진수를 10진수로 변환
    three_number = 0
    for j in range(len(three) - 1, -1, -1):
        three_number += three[j] * (3 ** (len(three) - 1 - j))
    return three_number

def three_decimal():
    three_numbers = []
    for i in range(len(three)):

        origin = three[i]

        if three[i] == 0:
            three[i] = 1
            three_numbers.append(three_to_ten())
            three[i] = 2
            three_numbers.append(three_to_ten())
        elif three[i] == 1:
            three[i] = 0
            three_numbers.append(three_to_ten())
            three[i] = 2
            three_numbers.append(three_to_ten())

        else: # 2
            three[i] = 0
            three_numbers.append(three_to_ten())
            three[i] = 1
            three_numbers.append(three_to_ten())

        three[i] = origin

    return three_numbers


for tc in range(1, int(input()) + 1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    #print(two, three)

    two_nums = two_decimal()
    three_nums = three_decimal()

    #print(two_nums, three_nums)

    if len(two_nums) < len(three_nums):
        for x in two_nums:
            if x in three_nums:
                print("#{} {}".format(tc, x))
    else:
        for x in three_nums:
            if x in two_nums:
                print("#{} {}".format(tc, x))