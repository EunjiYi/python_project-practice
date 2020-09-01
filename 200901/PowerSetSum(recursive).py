#함수에 sum하나만 추가해서 재귀로 넘겨주면 끝.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #arr의 부분집합 중 합이 10인 것 찾기
# 배열이 정렬되어있지 않아도 가능하다.
N = len(arr)
A = [0] * N # 0, 1

def powerset(n, k, cursum):
    if cursum > 10:
        return
    if n == k:
        print(A, end = ": ")
        for i in range(n):
            if A[i]:
                print(arr[i], end = " ")
        print()
    else:
        #k번째 선택
        A[k] = 1
        powerset(n, k+1, cursum + arr[k])

        #k번째 선택안함
        A[k] = 0
        powerset(n, k+1, cursum)

powerset(N, 0, 0)


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
