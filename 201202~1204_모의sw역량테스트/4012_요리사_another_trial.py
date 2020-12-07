def taste(foods):
    s = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            s += synergy[foods[i]][foods[j]]
            s += synergy[foods[j]][foods[i]]
    return s


def getS(n, a, b):
    global minV
    # (2) 모든 재료에 대해 결정한 경우, 식감을 계산한다.
    if n == N: # 모든 원소를 결정하고 난 뒤 식감을 계산한다.
        diff = abs(taste(A) - taste(B))
        if minV > diff:
            minV = diff
    else:
        # 아이디어:
        # (1) n번 재료를 A 또는 B 그릇에 넣는다.
        ## 0 <= n < N
        ## A와 B의 크기는 N//2
        ## 넣을 수 있는 쪽에만 넣는다.

        if a < N // 2:
            A.append(n) # A에 포함시킴
            getS(n+1, a+1, b) # A에 포함시켰으니 a원소갯수 하나 증가
            A.pop() # A에 포함시키지 않음
        if b < N // 2:
            B.append(n) # B에 포함시킴
            getS(n+1, a, b+1) # B에 포함시켰으니 b원소갯수 하나 증가
            B.pop() #B에 포함시키지 않음


for tc in range(1, int(input())+1):
    N = int(input())
    A = []
    B = []
    minV = 0xffffffff

    synergy = [list(map(int, input().split())) for _ in range(N)]

    getS(0, 0, 0)

    print("#{} {}".format(tc, minV))