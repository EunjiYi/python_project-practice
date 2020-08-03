def counting_sort(A, B, k):
    C = [0] * k

    #1단계 카운팅
    for i in range(0, len(B)):
        C[A[i]] +=1 #A의 값을 인덱스로 사용해서

    #2단계 누적
    for i in range(1, len(C)):
         C[i] += C[i-1]  #C[i] = C[i] + C[i-1]  #누적을 시켜라.

    #3단계 소트
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]   #여기 조심
        C[A[i]] -= 1

a = [0, 4, 1, 3, 1, 2, 4, 1]  #소스
b = [0] * len(a) #결과가 저장되는 배열
counting_sort(a, b, 4+1) # 10은 데이터의 범위가 나와있으면 그거 쓰면 됨.
print(a)
print(b)

