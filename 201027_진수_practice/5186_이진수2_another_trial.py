def decimal_to_binary(num):
    result = ""
    # 2를 곱하고 그 결과가 1보다 크면, 1을 뺀다
    cnt = 0
    while num:
        if cnt >= 13:
            result = "overflow"
            break
        tmp = num*2
        if tmp >= 1:
            result = result+"1"
            tmp = tmp -1
        else:
            result = result + "0"
        num = tmp
        cnt += 1

    return result


T= int(input())
for tc in range(1,T+1):
    num = float(input())
    print("#{} {}".format(tc,decimal_to_binary(num)))

