#아무것도 못 치고 멍때리고 20분 있었다...
#두려워하지말자, 어떻게 해야할지 모르겠으면 그냥 이렇게 말로라도 주절주절 적어보자.
#그리고 그 말로 적은 걸 한줄한줄 코드로 옮기자

# 1. 재귀함수를 써야겠다고 생각함.
# 2. 제일 처음이랑 마지막 글자가 같으면 그 다음부터 재귀돌리기
# 3. 기저조건 적어주기

#2번에서 막혔는데 슬라이싱하면 됐다!!!

# recursive

def is_pal_recursive(word):
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])
    else:
        return False

 
print(is_pal_recursive('tomato'))   #False
print(is_pal_recursive('racecar'))  #True
print(is_pal_recursive('azza'))  #True