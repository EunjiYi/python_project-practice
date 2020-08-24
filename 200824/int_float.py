str = "123"
str2 = "12.3"

print(int(str), type(int(str)))
print(float(str2), type(float(str2)))


test = "1+2"
print(test) #1+2
print(repr(test)) # 문자열을 ''로 감싸서 리턴 '1+2'
print(eval(test)) # 계산해서 리턴 3
print(eval(repr(test))) # 문자열이 벗겨져서 나옴 1+2
print(eval(eval(repr(test)))) # 당연 계산해서 3 나오겠지

# repr은 주로 개발자를 위한 것. ''로 감싸져서 나오니까 문자열인 것을 확인할 수 있어서.