def my_any(elements):
    for el in elements:
        if el:
            return True
    return False


#인간적으로 너무 헷갈림.
#원래 파이썬 내장함수 any():
    #인자로 받은 iterable(range, list)의 요소 중 하나라도 참이면 True반환, 비어있으면 False반환
'''
my_any([1, 2, 5, '6']) #=> True
my_any([[], 2, 5, '6']) #=> True
my_any([0]) #=> False
'''
print(my_any([]))   #False
print(my_any([1, 2, 5, '6']))   #True
print(my_any([[], 2, 5, '6']))   #True
print(my_any([0, '', []]))  #False
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))   #True  #True  #False