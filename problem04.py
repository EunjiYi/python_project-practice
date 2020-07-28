def dec_to_bin(n):
    #최종 결과를 반환할 빈 문자열
    strstr = ''
    while n > 1: # n이 0이나 1이 되기 전까지 반복문을 돌린다.
        strstr = str(n % 2) + strstr # n을 2로 나눈 나머지를 문자열 제일 뒤에 첨부한다. 
        n = n // 2 # 2로 나눴으므로 n은 2로 나눴을 때의 몫으로 바꿔주기
    strstr = str(n) + strstr # 마지막으로 남음 0 또는 1을 문자열 제일 앞에 첨부한다. 
    return strstr

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'