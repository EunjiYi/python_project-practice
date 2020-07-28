def swap(word):
    #결과를 출력할 빈 문자열 만들자
    strstr = ''
    for w in word:
        # 대문자면, 
        if ord(w) <= 90:
            #소문자로 바꾼다.
            strstr += chr(ord(w)+32)
        # 소문자면,
        else:
            #대문자로 바꾼다.
            strstr += chr(ord(w)-32)
    return strstr    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'