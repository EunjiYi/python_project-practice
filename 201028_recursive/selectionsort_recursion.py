arr = [3,2,5,1,4]
N = 5
#재귀를 이용한 반복문
def selection_sort(idx):
    if idx >= N-1:
        return
    #현재요소 이후에 있는 요소들 중에 가장 작은 값을 찾아서 현재요소와 자리를 바꿈
    min_v = arr[idx]  # 최소값과 위치 초기 값을 첫 요소로 설정
    min_idx = idx
    for i in range(idx, N):
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i

    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    print(arr)
    selection_sort(idx + 1) # 다음요소 정렬를 위한 호출

#현재 인덱스 이후에 잇는 요소중 가장 작은  값을 반환하는 재귀 함수
def min_value(idx):
    if idx == N-1:
        return (arr[N-1],idx)
    #이후에 요소들중 최소값을 반환하는 재귀 호출과 현재 요소중
    # 작은 값을 반환하면 됨
    tmp = min_value(idx+1)
    if arr[idx] < tmp[0]:
        return (arr[idx],idx)
    else:
        return tmp


def selection_sort2(idx):
    if idx >= N-1:
        return
    min_v, min_idx = min_value(idx)
    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    print(arr)
    selection_sort(idx + 1) # 다음요소 정렬를 위한 호출

selection_sort2(0)