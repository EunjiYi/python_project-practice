#정렬이 되어 있지 않은 경우
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n: return i
    else: return -1  #못찾았다 = False의 의미로 인덱스 줄 때 -1 많이 준다.
                    #파이썬에서는 -1가 마지막 인덱스를 가리키니까 조심하자.


arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(seq_search(arr, len(arr), key))


# 정렬이 되어있는 경우
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key: return i
    else: return -1  #못찾았다 = False의 의미로 인덱스 줄 때 -1 많이 준다.
                    #파이썬에서는 -1가 마지막 인덱스를 가리키니까 조심하자.


arr = [1,2,3,4,5,6,17,18,19]
key = 12 #17을 보고 빠져나가서 -1 찍는다.
print(seq_search(arr, len(arr), key))
