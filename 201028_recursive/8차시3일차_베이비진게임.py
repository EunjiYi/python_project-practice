# 가지고 있는 숫자를 비교해서 이긴 사람을 반환하는 함수
def isFinish(arr):
    for i in range(12):
        if arr[i] >= 3:
            return True
    for j in range(10):
        if arr[j] >= 1 and arr[j+1] >= 1 and arr[j+2] >= 1:
            return True
    return False

for tc in range(1, int(input())+1):
    card = list(map(int, input().split()))
    #print(card)

    A = [0] * 12
    B = [0] * 12

    result = 0
    for i in range(12):
        if i % 2 == 0: #1번이 가져감
            A[card[i]] += 1
            if isFinish(A):
                result = 1
                break
        else:
            B[card[i]] += 1
            if isFinish(B):
                result = 2
                break

    print("#{} {}".format(tc, result))