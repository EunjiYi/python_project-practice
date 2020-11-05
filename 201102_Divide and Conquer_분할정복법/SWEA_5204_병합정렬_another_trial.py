# 정렬하고자 하는 배열을 더 이상 나눌 수 없을 때 까지 절반으로 나눔
# 병합 : 각각의 배열을 앞쪽부터 순회하면서, 작은값을 새로운 배열에 복사
def merge_sort(arr):
    #나누기    길이가 1 초과 일때만 나누기
    if len(arr)  == 1:
        return arr
    mid = len(arr)//2
    #나눈 왼쪽부분 재귀 호출
    left = merge_sort(arr[:mid])
    #오른쪽 부분 재귀호출
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):  # left와 right를 병합
    global cnt
    # result = [-1] * (len(left)+len(right))
    result = list()
    # left와 right를 앞쪽부터 비교 하면서 작은 값을 result 에 추가 하기
    i = j = 0   #    앞쪽 부터 1씩 증가하는 인덱스

    if left[-1] > right[-1]:    #왼쪽 마지막 요소가 더 크면 카운트 증가
        cnt += 1

    # 하나의 배열이라도 복사할 요소가 남았으면 계속 반복
    while i < len(left) or j < len(right):
        #둘 다 복사가 끝나지 않았거나
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        #오른쪽 배열이 남아있으면,
        elif j < len(right):
            result.append(right[j])
            j += 1
        #왼쪽 배열이 남아있으면,
        elif i < len(left):
            result.append(left[i])
            i += 1

    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print("#{} {} {}".format(tc,arr[N//2],cnt))

