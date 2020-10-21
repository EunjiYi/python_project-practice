T = int(input())

for tc in range(1, T+1):
    inputlist = list(map(int, input().split()))
    cnt = inputlist[0] #구간의 갯수
    slicing = inputlist[1] # 구간
    numbers = list(map(int, input().split())) #숫자들

    maxValue = 0
    minValue = 500005
    for i in range(cnt-1):
        temp_numbers = numbers[i:i+slicing]
        if len(temp_numbers) != slicing:
            break;
        #print(temp_numbers)

        sum_temp_numbers = 0
        for j in range(slicing):
            sum_temp_numbers += temp_numbers[j]
            #print(sum_temp_numbers)


        if sum_temp_numbers >= maxValue:
            maxValue = sum_temp_numbers
            #print(maxValue)


        if sum_temp_numbers <= minValue :
            minValue = sum_temp_numbers
            #print(minValue)

    print('#{} {}'.format(tc, maxValue-minValue))