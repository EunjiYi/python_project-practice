#문자열 비교
T = int(input())
for tc in range(1,T+1):
    result = 0
    str1 = input()
    str2 = input()

    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
        else: #break가 걸리지 않음 = 문자열이 존재
            result = 1
            break

    print("#{} {}".format(tc,result))