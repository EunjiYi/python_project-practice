T = int(input())

for tc in range(1, T + 1):
    num_of_numbers = int(input())
    numbers = list(map(int, input().split()))

    max = numbers[0]
    min = numbers[0]
    for j in range(num_of_numbers):
        if numbers[j] > max:
            max = numbers[j]
        if numbers[j] < min:
            min = numbers[j]

    print('#{} {}'.format(tc, max - min))

#min max count 쓰지말자 연습이니까.
    # T = int(input())
    #
    # for i in range(1, T + 1):
    #     num = int(input())
    #     listlist = list(map(int, input().split()))
    #
    #     print('#{} {}'.format(i, max(listlist) - min(listlist)))