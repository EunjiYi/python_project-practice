#left,right :시작,종료 인덱스
#target : 찾고자하는 변수
#dir : 이전 단계에서 이동한 방향 1 왼쪽, 2 오른쪽
def binary_search(left,right,target,dir):
    global cnt
    mid = (left+right)//2
    if A[mid] == target:
        # 더 이상 검사를 할 필요가 없음, 찾았으면, 왼쪽오른쪽을 번갈아 가면서 찾은 숫자이다.
        cnt += 1

    elif A[mid]  > target:  # 뒤쪽은 검사할 필요가 없음, 왼쪽검사해야함
        if dir == 1:
            return
        binary_search(left,mid-1,target,1)

    elif A[mid] < target: # 앞쪽을 검사할 필요가 없음, 오른쪽 검사해야함
        if dir == 2:
            return
        binary_search(mid+1,right, target, 2)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)   #정렬
    cnt = 0
    # B에 속한 요소들이 A에 있는지 검사하면서, 조건에 부합하는지 확인
    for i in B:
        if i in A:  #i 가 A에 포함된다면, 조건에 부합하는지 검사
            #이진 탐색 시작
            binary_search(0,N-1,i,0)

    print("#{} {}".format(tc,cnt))