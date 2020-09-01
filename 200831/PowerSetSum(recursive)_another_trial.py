# 멱집합 : 모든 부분집합
# 조합  : 특정 조건을 만족하는 부분집합
# 순열 : 요소들의 순서정렬

# 부분집합의 합이 5이하인 부분집합을 모두 출력하라
arr = [6,5,3,1,4,2]
N = len(arr) #총 원소 갯수
S = 5
selected = [0] * N
# 각 요소가 부분집합에 포함되는지 표시하는 배열 (0, 1)

# 현재 인덱스 요소를 포함할지, 안할지를 나타내는 함수
def powerset(idx, sum):
    if sum > S:
        return

    if idx == N:
        #print(selected)
        for i in range(N):
            if selected[i] == 1:
                print(arr[i], end=" ")
        print()
        return

    #현재 상태에서 실행할 수 있는 모든 경우의 수(현재요소를 포함하거나, 포함하지 않거나) 실행
        #현재요소 포함
    selected[idx] = 1
    powerset(idx + 1, sum + arr[idx])

    #현재요소 미포함
    selected[idx] = 0
    powerset(idx + 1, sum)

    # for i in range(2):
    #     selected[idx] = i
    #     powerset(idx+1)


powerset(0, 0)







