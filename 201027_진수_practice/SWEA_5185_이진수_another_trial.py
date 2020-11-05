hex_dic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14 ,"F":15  }
def hex_to_decimal(str,n):
    result = 0  # 각자리수 계산 값을 더할 변수
    cnt= n-1
    for i in range(n):
        result +=(hex_dic[str[i]] *(16**cnt))
        cnt -= 1
    return result

def decimal_to_binary(n,length):
    binary = [0] *(length*4)
    idx = length*4-1
    while n > 0:
        # n을 2로 나누어서 나머지를 계속 저장
        binary[idx] = n % 2
        idx -= 1
        n = n//2
    return binary

T = int(input())
for tc in range(1,T+1):
    N, hex = input().split()
    N = int(N)
    #16진수 문자열을 10진수로 바꾸기
    num = hex_to_decimal(hex,N)
    # print(num)
    result= decimal_to_binary(num,N)
    print(result)