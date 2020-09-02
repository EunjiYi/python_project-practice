#함수에 sum하나만 추가해서 재귀로 넘겨주면 끝.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #arr의 부분집합 중 합이 10인 것 찾기
# 배열이 정렬되어있지 않아도 가능하다.
N = len(arr)
A = [0] * N # 0, 1
total = 0
def powerset(n, k, cursum): #n:원소의 갯수, k: 현재의 depth
    global total
    #############여기가 가지치기 부분 ##########
    if cursum > 10:
        return
    #############가지치기의 방법은 문제마다 조금씩 다 다르다 다양한 문제 접하기 ##########
    total += 1
    if n == k:      # Basis Part
        print(A, end = ": ")
        for i in range(n):  # 각 부분배열의 원소를 출력
            if A[i]:        # A[i]가 1이면 포함된 것이므로 출력
                print(arr[i], end = " ")
        print()
    else:           # Unductive Part
        #k번째 선택
        A[k] = 1
        powerset(n, k+1, cursum + arr[k])  # 다음 요소 포함 여부 결정

        #k번째 선택안함
        A[k] = 0
        powerset(n, k+1, cursum)  # 다음 요소 포함 여부 결정

powerset(N, 0, 0)
print("호출횟수 : {}".format(total))

'''
출력
[1, 1, 1]: 1 2 3 
[1, 1, 0]: 1 2 
[1, 0, 1]: 1 3 
[1, 0, 0]: 1 
[0, 1, 1]: 2 3 
[0, 1, 0]: 2 
[0, 0, 1]: 3 
[0, 0, 0]: 
'''
