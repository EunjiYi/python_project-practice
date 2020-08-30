#선택정렬
arr = [64, 25, 10, 22, 11]
N = len(arr)

for i in range(N):  #0, n-1까지
    idx = i    #시작위치 지정
    if i % 2 == 0:
        for j in range(i + 1, N):
            if arr[idx] < arr[j]:
                idx = j

    else:
        for j in range(i + 1, N):
            if arr[idx] > arr[j]:
                idx = j

    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)

#인덱스만 저장해 놓고 else까지 다 끝나고 교환해도된다. if/else문에 각각 교환하는 것 넣을 필요 없다.

#다 정렬해놓고 가져오는 방식은 배열의 요소 갯수가 많아지면 곤란.
# 이 방식으로 하면 10번만 하면되잖아.