
def bin_search(a, key):
    start = 0
    end = len(a)
    while start <= end:
        middle = (start + end) // 2   #파이썬 조심 / 하나만 쓰면 2.xxx나온다.
        # ==
        if a[middle] == key:
            return True, middle
        # >
        elif a[middle] > key:
            end = middle - 1
        # <
        else:
            start = middle + 1
    return (False, -1) #파이썬만 된다! 리턴값을 튜플로 값을 2개 받을 수 있징!
                        #괄호 치나, 안치나 어차피 리턴시 ()로 묶여서 나옴.


arr = [2, 4, 7, 9, 11, 19, 23]
key = 18
print(bin_search(arr, key))