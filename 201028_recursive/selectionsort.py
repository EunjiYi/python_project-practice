# 선택 정렬
# 가장 작은(혹은 가장 큰) 요소를 가장 앞에다
# 가져다 놓는 작업을 반복하며 정렬
arr = [3,2,5,1,4]
N = 5
#0~3번 인덱스에 들어갈 값을 찾아서 넣는 작업을 반복해야 한다.
for j in range(N-1):
    #1. 가장 작은 요소를 찾는다.
    min_v = arr[j]  # 최소값과 위치 초기 값을 첫 요소로 설정
    min_idx = j
    for i in range(j,N):
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i
    #2. 가장 작은 요소를 가장 앞 요소와 자리를 바꾼다.
    arr[j],arr[min_idx] = arr[min_idx],arr[j]
    print(arr)

