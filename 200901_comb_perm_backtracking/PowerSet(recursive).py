# {1,2,3} 모든 부분 집합 출력하기
arr = [1, 2, 3]
N = len(arr)
A = [0] * N #원소의 포함여부를 저장 (0, 1)

def powerset(n, k):  #n:원소의 갯수, k: 현재 depth
    if n == k:   # basis condition
        print(A, end = ": ")
        for i in range(n):  #각 부분 배열의 원소 출력
            if A[i]:         #A[i]가 1 이면 포함된 것이므로 출력
                print(arr[i], end = " ")
        print()
    else:   #Inductive Part
        #k번째 선택  
        A[k] = 1            #k번 요소 포함
        powerset(n, k+1) # 다음 요소 포함 여부 결정

        #k번째 선택안함
        A[k] = 0	# k번 요소 포함 안함
        powerset(n, k+1)  # 다음 요소 포함 여부 결정

powerset(N, 0)


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
