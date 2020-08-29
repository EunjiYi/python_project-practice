for tc in range(1, int(input()) + 1):
    arr = input()
    S = []

    for ch in arr:
        if not S or ch != S[-1]: #단축평가에 의해 앞 조건만 검사하고 넘어갈 수도 있다.
                                # 그런데 이렇게 쓰다가 실수가 날 수 있다.
                                # 코드는 최대한 완전하게(정확하게) 모든 경우의 수 다 따져서 짜자. 간결함은 그 뒤에.
            S.append(ch)
        else:
            S.pop()
        print(len(S))