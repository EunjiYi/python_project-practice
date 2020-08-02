def my_all(elements):
    #뽑아낼 요소가 아예 없으면 (비어있으면 for문 돌지 않는다.)
    for el in elements:
        if not el: #값이 없는 경우
            # if el 이면 값이 있을 때 true
            return False
    return True

#인간적으로 너무 헷갈림.
#원래 파이썬 내장함수 all() : 
    #인자로 받은 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True반환

#예시를 봐도 헷갈림
'''
my_all([]) #=> True
my_all([1, 2, 5, '6']) #=> True
my_all([[], 2, 5, '6']) #=> False
'''
print(my_all([]))  #True
print(my_all([1, 2, 5, '6']))   #True
print(my_all([[], 2, 5, '6']))  #False
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))  #True  True  False
print(my_all([0, '', []]))   #False
