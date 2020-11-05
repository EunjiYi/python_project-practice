def quick_sort(start,end):
    if start < end:
        # 파티션나누기  : 피벗 정하고, 피벗을 기준으로 작은값과 큰값으로 구분하기
        pivot = partition(start,end)
        # 작은 값 부분 다시 퀵소트
        quick_sort(start,pivot-1)
        # 큰 값 부분 다시 퀵소트
        quick_sort(pivot+1, end)

def partition(start,end):
    # number를 pivot 기준으로 큰 값과 작은 값으로 나누기
    pivot = numbers[start]
    i = start
    j = end
    while i <= j:
        # i를 증가 시키면서 pivot보다 큰 값 찾기
        while i <= j and numbers[i] <= pivot:
            i += 1
        while numbers[j] > pivot:
            j -= 1
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[start], numbers[j] = numbers[j], numbers[start]
    return j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    quick_sort(0,N-1)
    print("#{} {}".format(tc,numbers[N//2]))


