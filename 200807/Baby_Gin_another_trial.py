#Baby-Gin
#원소수가 3개인 부분집합을 생성
# 1이 3개인 6자리 2진수 -> 0도 3개

cards = [5, 4, 1, 2, 3, 6]
cards.sort() # 정렬하고 뽑으면 크기순으로 가능.
for subset in range(1 << 6):

    A, B = [], []
    # 각 자리 값을 확인
    for i in range(6):
        if subset & (1 << i):
            A.append(cards[i])
        else:
            B.append(cards[i])

    if len(A) == len(B):
        print(A, B) #이렇게 하면 중복된거 포함됨. -> 중복제거하고싶다? 생각해보기.
