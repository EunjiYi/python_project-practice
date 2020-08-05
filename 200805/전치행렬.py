
'''
3 3
1 2 3
4 5 6
7 8 9
'''
N, M = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(N)]

#1
for i in range(N):
    for j in range(M):
        if i < j:  #이게 없으면 대각선으로 두 번 swap해버려서 원래 배열(그대로)이 나옴.
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)

#2
for i in range(N):
    for j in range(i+1, M):
        #if i < j:  #if 없애려면 j 의 range를 바꾼다.
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)


#3
#전치행렬로 조합도 구할 수 있다.
# 1, 2, 3, 4 해서 2개씩 고르는 거 만들기
arr = [1, 2, 3, 4]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        print((arr[i], arr[j]), end = " ")
        #답 (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)

        