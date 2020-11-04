#퀵정렬
# partition (파티션) : 피벗을 하나 정해서, 큰 값과 작은값들로 구분하는 기능
# 재귀 호출 부분 : 큰값과 작은값의 부분들을 각각 다시 퀵정렬 호출
def quick_sort(arr,left,right):
    if left < right:
        #파티선 나누고
        pivot = partition(arr,left,right)
        #왼쪽 부분 호출
        quick_sort(arr,left,pivot-1)
        #오른쪽 부분 호출
        quick_sort(arr, pivot+1, right)

def partition(arr,left,right):
    #피벗 잡고
    # 피벗보다 작은값을 앞쪽으로
    # 피벗 보다 큰 값을 뒤쪽으로
    i = left
    j = right
    pivot = arr[left]

    while i <= j:
        while i <= j and arr[i] <= pivot :
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr,0,N-1)
    print("#{} {}".format(tc,arr[N//2]))
