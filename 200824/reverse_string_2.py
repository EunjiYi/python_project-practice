#문자열 뒤집기
a = "Reverse this sentence"
reversed_str = list()

#길이가 N인 배열/문자열은 0~N-1
# for(초기화;조건;조건증감)
# for(int i=0; i<5; i++): 자바
#문자열을 뒤에서부터 한 인덱스씩 줄여가면서 조회
for i in range(len(a)-1, -1, -1): # -1이 포함되지 않음 그니까 0까지 도는 것.
    #print(a[i], end="")
    reversed_str.append(a[i])
print(reversed_str)

#복사
b = a[::-1]
print("b: {}".format(b))

#다른 방법 #reverse 함수
c = reversed(a)
print(list(c))  # print(c)가 아니고 print(list(c))해야함.
#reversed 함수 자체가 반복적인 리턴값을 주는 형태라 그냥 print(c)찍으면 그 주소를 반환한다.
#그 '반복적인 리턴값'을 리스트로 만들어서 출력해줘야한다.


str2 = "algorithm"
arr2 = list(str2)
arr2.reverse()
str2 = "".join(arr2)
print(str2)