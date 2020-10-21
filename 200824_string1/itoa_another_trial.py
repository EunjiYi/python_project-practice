def itoa(num):
    x = num # 몫
    y = 0 # 나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10  # x //= 10
        #arr.append(chr(y + ord('0'))) 이런 방법 아니면, #str = "".join(arr) 없애고 바로 아래줄처럼 할 수 있다.
        arr.append(y)

    arr.reverse()
    #str = "".join(arr)
    #return str
    return arr

x = 123
print(x, type(x))
str = itoa(x)
print(str, type(str))