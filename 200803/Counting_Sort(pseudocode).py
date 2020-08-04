def Counting_Sort(A, B, k) #k는 최댓값
# A [] -- 입력배열(1 to k) 원본
# B [] -- 정렬된 배열 temp
# C [] -- 카운트 배열 counts

C = [0] * k # k갯수만큼 counts를 초기화

for i in range(0, len(B)): #카운팅됨.
    C[A[i]] += 1

for i in range(1, len(C)): #누적, 1부터해야되는거 잊지말고!
    C[i] += C[i-1]

for i in range(len(B)=1,-1, -1): #맨뒤에서부터 0까지
    B[C[A[i]]-1] = A[i]  #인덱스가 0부터 시작하니까 -1해준거고, temp에 담는 단계
    C[A[i]] -= -1 #temp에 담고 counts에서 1 빼는 단계
