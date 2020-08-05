def selection(a, k):   #총 3군데만 달라 여기랑
    # i:0 ~ len(n)-1
    for i in range(k): #여기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:    #if a[min] < a[j]:  이렇게만 하면 k번째로 큰 값.
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1] #여기

def selectionSort(a):
    # i:0 ~ len(n)-1
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:    #if a[min] < a[j]: 로 바꾸면 [64, 25, 22, 11, 10]
                min = j
        a[i], a[min] = a[min], a[i]

arr = [64, 25, 10, 22, 11]
selectionSort(arr)
print(arr)
# [10, 11, 22, 25, 64]
print(selection(arr, 2))
# 11 = K번째로 작은 값