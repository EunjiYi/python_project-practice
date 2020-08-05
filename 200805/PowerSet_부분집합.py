#이건 부분집합을 완전검색(for문)으로 푸는 방법이다.
#그런데 가지치기는 안된다. 가지치기는 재귀로 해야한다.

def printList(arr, bit):
    for i in range(len(bit)): #bit의 수만큼 돌리자.
        if bit[i]: #bit가 1이면 그거에 해당하는값 출력하기
            print(arr[i], end = " ")
    print()


arr = [1,2,3]
bit = [0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            printList(arr, bit)
            #print(bit) 여기서 bit찍으면
            # [0, 0, 0] {} 이건 공집합
            # [0, 0, 1] {3}
            # [0, 1, 0] {2}
            # [0, 1, 1] {2,3}
            # [1, 0, 0] {1}
            # [1, 0, 1] {1,3}
            # [1, 1, 0] {1,2}
            # [1, 1, 1] {1,2,3}
