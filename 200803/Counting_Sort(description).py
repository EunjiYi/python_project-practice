def counting_sort(A, B, k):
    C = [0] * k
    #카운팅
    for i in range(0, len(B)): # len(A)도 가능
        C[A[i]] += 1 # A의 값을 인덱스로 사용해서 1 증가 시켜라.

    #누적
    for i in range(1, len(C)):
        C[i] += C[i-1]  #C[i] = C[i] + C[i-1]

    #소트(자기자리 찾아가기, 결과, 저장)
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
counting_sort(a, b, 4+1) #인덱스니까 +1, 하나 더 크게 받는다.

print(a)
print(b)