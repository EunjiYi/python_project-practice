def caesar(word, n):
    # 최종 결과를 출력할 빈 문자열 변수 만들기
    strstr = ''
    # chr(num) <= chr 안에 들어갈 값
    num = 0
    for w in word: # 대소문자 구분하자.
        #input값이 대문자일 때
        if 65 <= ord(w) <= 90:
            if ord(w) + n > 90: 
                # 원래 아스키 코드 값과 n을 더했을 때 
                # 대문자아스키코드 영역(65~90)을 넘어갈 경우 다시 순회.
                num = ord(w) + n - 26
            else:
                num = ord(w) + n
        #input값이 소문자일 때
        else:
            if ord(w) + n > 122: 
                # 원래 아스키 코드 값과 n을 더했을 때 
                # 소문자아스키코드 영역(97~122)을 넘어갈 경우 다시 순회.
                num = ord(w) + n - 26
            else:
                num = ord(w) + n
        strstr += chr(num) # 최종적으로 반환할 값
    return strstr   

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'