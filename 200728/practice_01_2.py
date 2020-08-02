# while
# 그냥 반복문으로도 할 수 있다.

def is_pal_while(word):
    
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]  ### 이렇게 슬라이싱 한 걸 워드에 다시 넣어주면 되지!! 왜 나는 이런 생각을 못하지... 멍청해
        else:
            return False
    return True

print(is_pal_while('tomato'))   #False
print(is_pal_while('racecar'))  #True
print(is_pal_while('azza'))     #True