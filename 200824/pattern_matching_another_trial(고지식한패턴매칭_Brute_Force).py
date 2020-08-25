#고지식한 패턴매칭
#주어진 문자열안에 특정 pattern이 존재하는지 여부를 출력하는
#프로그램 작성

str = "Hello world! Nice to meet you"
pattern = "world"

#target 안에서 pattern을 찾으면 True, 아니면 False 반환
# [][][][][][]  : 6
# [][][] : 3
# len(target) - len(pattern) + 1
def search(target,pattern):
    for i in range(len(target)-len(pattern) + 1):
        for j in range(len(pattern)):
            #똑같으면 다음 거 비교 진행,
            # 다르면 즉시 종료
            if pattern[j] != target[i+j]:
                    break
        else:   # for 반복문에서 break가 한 번도 안걸리면, #반복문이 break없이 완전하게 종료되었다면
            # 패턴 찾음
            return True
        # 위 작은 반복문에서 break가 걸리면,
        # 해당비교에서 pattern을 못찾음
    return False

result = search(str,pattern)
print(result)


