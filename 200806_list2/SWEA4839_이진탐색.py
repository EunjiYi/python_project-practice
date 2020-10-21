T = int(input())
for tc in range(1, T+1):
    def bin_search(key):
        start = 1
        end = P
        cnt = 0
        while start <= end:
            cnt += 1
            middle = (start + end) // 2   #파이썬 조심 / 하나만 쓰면 2.xxx나온다.
            # ==
            if middle == key:
                return cnt
            # >
            elif middle > key:
                end = middle
            # <
            else:
                start = middle
        #return 탐색에 실패할 경우인데, 여기서는 실패할 수 없으므로 생략

    P, A, B = map(int,input().split())
    # arr = list(range(0, P+1)) #인덱스랑 값이랑 같다!
    A_value = bin_search(A)
    B_value = bin_search(B)

    print('#{}'.format(tc), end = " ")
    print('A' if A_value < B_value else 'B' if A_value > B_value else '0')