#2차원 리스트 90도로 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이 계산
    m = len(a[0]) #열 길이 계산

    result = [[0] * n for _ in range(m)]  # 결과리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

arr = [[1,2,3], [4,5,6]]
print(rotate_a_matrix_by_90_degree(arr))  # [[4, 1], [5, 2], [6, 3]]