def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        # 0~9
        # if c >= '0' and c <= '9': 이것도 되고 파이썬은 아랫것도 된다.
        if '0' <= c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = value * 10 + digit # 만약 a=[1,2,3]이면 digit 구할필요없이 여기가 str[i]이면 끝.
    return value


a = "123"
print(type(a))

b = atoi(a)
print(b, type(b))